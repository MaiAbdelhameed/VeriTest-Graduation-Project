import sys
sys.path.append("..")
from PARSER.graph import parse_verilog
import matplotlib.pyplot as plt
from Coverage.random_stimuli import random_stimuli
from Coverage.random_stimuli import Insert_Random_Input
from PARSER.preprocessing.find import get_input_output
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
import random
from PARSER.components.Gates.bitwise import bitwise

import networkx as nx
from pyverilog.vparser.ast import *
import pyverilog.vparser.ast as ast
from PARSER.code_to_graph import code_to_graph
from PARSER.GraphAPI import GraphAPI
from z3 import *
import json
import re

class My_Block:
    def __init__(self, block_id):
        self.block_id = block_id
        self.statements_list = []
        self.blocks_list = []
        self.all_conds = list()
        #self.type = type
        self.cond = []

    def __str__(self):
        # Convert the list of tuples to a string representation
        statements_str = "\n".join(str(statement) for statement in self.statements_list)

        # Convert the list of block objects to a string representation
        objects_str = "\n".join(str(obj.block_id) for obj in self.blocks_list)

        # Construct the complete string representation of the block
        block_str = f"Block ID: {self.block_id}\nCondition: {self.cond}\nStatements List:\n{statements_str}\nObjects List:\n{objects_str}"

        return block_str

id = 1
flowbreak_statements = [IfStatement, CaseStatement , Repeat, ForStatement, DelayStatement, Disable, TaskCall, FunctionCall]
flag = False
flag2 = False


def SaveJson(dict_before, dict_after, file):
    with open("output/" + file +".json", "w") as out:
        list_of_dicts = list()
        list_of_dicts.append(dict_before)
        list_of_dicts.append(dict_after)
        json.dump(list_of_dicts, out)
        

   
    

def parse_coverage_always(obj, G, branch, parent=None,conditions=None):
    global id  # Declare id as global to modify it within the function
    global flag
    global flag2
    if obj is None:
        return None

    if isinstance(obj, Block):
        if (branch != 1 or (conditions is not None)):
            block = My_Block(block_id=id)
            id += 1  # Increment id
            block.cond = conditions
            flag = False
        for x in obj.statements:
            if(branch == 1):
                if (conditions is not None):
                    a = parse_coverage_always(x, G, branch, parent=block)  # Pass root as parent
                else:
                    a = parse_coverage_always(x, G, branch, parent)  # Pass root as parent
            else:
                a = parse_coverage_always(x, G, branch, parent=block)  # Pass current block as parent
                if a is None:
                    if flag2 is False:
                        block.statements_list.append((str(x.left.var) + '=' + str(x.right.var),x.lineno))
                    else:
                        if block.blocks_list and isinstance(block.blocks_list[-1], My_Block):
                        # Access the statements_list attribute of the last My_Block object in blocks_list
                            block.blocks_list[-1].statements_list.append((str(x.left.var) + '=' + str(x.right.var),x.lineno))
        if(branch != 1 or (conditions is not None)):
            return block
        else:
            return

    elif isinstance(obj, NonblockingSubstitution) or isinstance(obj, BlockingSubstitution):
        if flag is True:
            block = My_Block(block_id=id)
            block.cond = conditions
            if (branch != 1):
                block.statements_list.append((str(obj.left.var) + '=' + str(obj.right.var),obj.left.lineno))
            id += 1  # Increment id
            flag = False
            flag2 = True
            G.add_node(block)  # Add node for the My_Block object
            if parent is not None:
                G.add_edge(parent, block)  # Add edge from parent to block
                parent.blocks_list.append(block)
            return block
        else:
            return None

    elif isinstance(obj, IfStatement):
        flag = True
        flag2 = False
        if obj.false_statement is None:
            if conditions is None:
                conditions = [] 
            conditions.append((1,obj.cond))
            true_block = parse_coverage_always(obj.true_statement, G, branch, parent,conditions[:])
            flag = True
            G.add_node(true_block)  # Add node for true block
            if parent is not None:
                G.add_edge(parent, true_block)  # Add edge from parent to true block
            return true_block
        else:
            if conditions is None:
                conditions = [] 
            conditions.append((1,obj.cond))
            true_block = parse_coverage_always(obj.true_statement, G, branch, parent,conditions[:])
            flag = True
            flag2 = False
            conditions[-1] = (0,obj.cond)
            false_block = parse_coverage_always(obj.false_statement, G, branch , parent,conditions[:])
            flag = True
            flag2 = False
            if true_block is not None:
                G.add_node(true_block)  # Add node for true block
                if parent is not None:
                    G.add_edge(parent, true_block)  # Add edge from parent to true block
                    if true_block not in parent.blocks_list:
                        parent.blocks_list.append(true_block) ##
            if false_block is not None:
                if isinstance(false_block,tuple): # handles if else if instances
                    blocks = (true_block,)
                    for item in false_block:
                        G.add_node(item)
                        blocks + (item,)
                        if parent is not None:
                            G.add_edge(parent, item)  # Add edge from parent to false block
                    return blocks
                else:
                    G.add_node(false_block)  # Add node for false block
                    if parent is not None:
                        G.add_edge(parent, false_block)  # Add edge from parent to false block
            return (true_block,false_block)  # Return only one block for IfStatement
    
    elif isinstance(obj, CaseStatement):
        all_conditions = [] 
        flag = True
        flag2 = False
        for case in obj.caselist:
            if case.cond is None:
                block = parse_coverage_always(case.statement,G,branch,parent,all_conditions)
                flag = True
                flag2 = False
            else:
                all_conditions.append((0,case.cond,str(obj.comp)))
                if isinstance(case.statement,CaseStatement) or isinstance(case.statement,IfStatement):
                    new_parent = My_Block(block_id=id)
                    new_parent.cond = [(1,case.cond,str(obj.comp))]
                    id += 1  # Increment id
                    G.add_node(new_parent)  # Add node for true block
                    if parent is not None:
                        G.add_edge(parent, new_parent)  # Add edge from parent to block
                        if new_parent not in parent.blocks_list:
                            parent.blocks_list.append(new_parent)
                    parse_coverage_always(case.statement,G,branch,new_parent)
                    flag = True
                    flag2 = False
                else:    
                    block = parse_coverage_always(case.statement,G,branch,parent,[(1,case.cond,str(obj.comp))])
                    flag = True
                    flag2 = False
                    if block is not None:
                        G.add_node(block)  # Add node for true block
                        if parent is not None:
                            G.add_edge(parent, block)  # Add edge from parent to block
                            if block not in parent.blocks_list:
                                parent.blocks_list.append(block) 
        return block

#id = 11
def parse_assigns(obj, G, left,parent=None,conditions=None):
    global id
    try:
    # Code that might raise an exception
        obj.cond
    except Exception as e: # no condition
        # If there was no condition, hence add it to assign_block
        block = My_Block(block_id=id)
        id+=1
        block.cond = conditions
        block.statements_list.append((str(left) + '=' + str(obj.value),obj.lineno))
        G.add_node(block)  # Add node for the My_Block object
        if parent is not None:
            G.add_edge(parent, block)  # Add edge from parent to block
            parent.blocks_list.append(block)
        return block
    else:
        if conditions is None:
                conditions = [] 
        conditions.append((1,obj.cond))
        try:
        # Code that might raise an exception
            obj.true_value.cond
        except Exception as e: # no condition
            true_block = parse_assigns(obj.true_value, G ,left,parent,conditions[:])
        else:
            block = My_Block(block_id=id)
            id+=1
            block.cond = conditions[:]
            #block.statements_list.append((str(obj.left.var) + '=' + str(obj.right.var.true_value),obj.right.lineno))
            G.add_node(block)  # Add node for the My_Block object
            if parent is not None:
                G.add_edge(parent, block)  # Add edge from parent to block
                parent.blocks_list.append(block)
            true_block = parse_assigns(obj.true_value, G ,left ,block,None)

        conditions[-1] = (0,obj.cond)
        # Code to execute if no exception occurs
        false_block = parse_assigns(obj.false_value, G,left ,parent,conditions[:])


def convert_to_binary(fin_value, type_of_value):
    hex_map = {hex(i)[2:].upper(): f"{bin(i)[2:]:>04}" for i in range(16)}
    if type_of_value == "b":
        return fin_value
    elif type_of_value == "h":
        return "".join(hex_map.get(hex_digit) for hex_digit in fin_value)
    elif type_of_value == "d":
        return bin(int(fin_value))[2:]
    
def convert_to_decimal(binary):
    binary = str(binary)
    s = 0
    for index, bit in enumerate(reversed(binary)):
        s += int(bit) * pow(2, index)
    return int(s)

def Generate_SMT_cond(cond, input_output_wire, list_of_all_Z3_vars, decompose = False):

    if isinstance(cond,Partselect):
        msb = cond.msb.value
        lsb = cond.lsb.value
        size = abs(int(msb) - int(lsb)) + 1
        new_vec = BitVec(cond.var.name+"["+ msb+ ":" +lsb + "]", size)
        return new_vec
    

    if isinstance(cond, ast.And) or isinstance(cond, ast.Land):
        left = Generate_SMT_cond(cond.left, input_output_wire, list_of_all_Z3_vars)
        right = Generate_SMT_cond(cond.right, input_output_wire, list_of_all_Z3_vars)


        return z3.And(left, right)
    if isUgate(cond):
        right = Generate_SMT_cond(cond.right, input_output_wire, list_of_all_Z3_vars, decompose = True)
        stack = list()
        stack.append(right[0])
        right.remove(right[0])
        if isinstance(cond, Uand):
            for bit in right:
                UAND = z3.And(bit, stack[-1])
                stack.append(UAND)
        if isinstance(cond, Uand):
            for bit in right:
                UOR = z3.Or(bit, stack[-1])
                stack.append(UAND)



        return stack[-1]
        

    
    if isinstance(cond, ast.Or) or isinstance(cond, ast.Lor):
        left = Generate_SMT_cond(cond.left, input_output_wire, list_of_all_Z3_vars)
        right = Generate_SMT_cond(cond.right, input_output_wire, list_of_all_Z3_vars)


        return z3.Or(left, right)
    
    elif isinstance(cond,Pointer):
        if cond.var.name in list_of_all_Z3_vars:
            return list_of_all_Z3_vars[cond.var.name]
        
        new_vec = BitVec(cond.var.name+"["+ cond.ptr.value + "]", 1)
        list_of_all_Z3_vars.update({cond.var.name: new_vec})
        return new_vec

    elif isinstance(cond,Identifier):
        if cond.name in list_of_all_Z3_vars and not decompose:
            return list_of_all_Z3_vars[cond.name]
        size = 0
        if cond.name in input_output_wire[0]:
            size = input_output_wire[0][cond.name]
        
        if cond.name in input_output_wire[1]:
            size = input_output_wire[1][cond.name]

        if cond.name in input_output_wire[2]:
            size = input_output_wire[2][cond.name]

        if cond.name in input_output_wire[3]:
            size = input_output_wire[3][cond.name]

        if not decompose:
            x = BitVec(cond.name,size)
            list_of_all_Z3_vars.update({cond.name: x})
            return x
        else:
            list_of_vars = list()
            for i in range(size):
                if cond.name+'[' + str(i) + ']' in list_of_all_Z3_vars:
                    list_of_vars.append(list_of_all_Z3_vars[cond.name+'[' + str(i) + ']'])
                else:
                    x = Bool(cond.name+'[' + str(i) + ']')
                    list_of_all_Z3_vars.update({cond.name+'[' + str(i) + ']': x})
                    list_of_vars.append(x)
            return list_of_vars


    
        # Base case: Operand is an identifier (input variable)
        # Retrieve the value of the input variable from input_values dictionary
       

    elif isinstance(cond, IntConst):
        value = cond.value
        value = re.sub("_","",value)
        fin_value = re.search(r"(?:\d*'\w)?(\d+|\w+)", value).group(1)
        fin_value2 = re.search(r"(\d*)?(?:'\w)?(?:\d+|\w+)", value).group(1)
        type_of_value = re.findall("\d+'(\w)(?:\d+|\w+)", value)
        if len(type_of_value) == 0: type_of_value = "d"
        else: type_of_value = type_of_value[0]
        fin_value = convert_to_binary(fin_value, type_of_value)
        if fin_value2 == '':
            fin_value2 = 1
        fin_value = (str(0) * (int(fin_value2) - len(str(fin_value)))) + str(fin_value)
        fin_value = int(fin_value)
        fin_value = convert_to_decimal(fin_value)
        return fin_value
    # Case statements
    elif isinstance(cond, tuple) and (len(cond) == 1):
        # Base case: Operand is an integer constant
        pass

    elif isinstance(cond, Operator):
        # Recursive case: Operand is an operator node (e.g., GreaterThan, Eq, Lor, Land)
        # Evaluate the left and right sub-expressions recursively
        left_result = Generate_SMT_cond(cond.left, input_output_wire, list_of_all_Z3_vars)
        right_result = Generate_SMT_cond(cond.right, input_output_wire, list_of_all_Z3_vars)

        if isinstance(cond, GreaterEq):
            return UGE(left_result, right_result)
        elif isinstance(cond, GreaterThan): # el ba2y
            return UGT(left_result, right_result)
        elif isinstance(cond, LessThan): # el ba2y
            return ULT(left_result, right_result)
        elif isinstance(cond, LessEq): # el ba2y
            return ULE(left_result, right_result)
        elif isinstance(cond, Eq): # el ba2y
            try:
                return left_result == right_result
            except:
                return left_result == bool(right_result)

            
        elif isinstance(cond, NotEq): # el ba2y
            try:
                return left_result != right_result
            except:
                return left_result != bool(right_result)




def toggle_coverage(input_output_wire, input_test_cases, num_of_test_cases, index):
    dict_of_flatten_bits = dict()
    dict_of_inputs = dict()
    for key, value in input_output_wire[0].items():
        ll = dict()
        x = None
        dict_of_inputs.update({key: x})
        dict_of_flatten_bits.update({key: ll})
        for i in range(value):
            value = re.search("\d+'b(.*)",input_test_cases[key][index]).group(1)
            value = value[::-1]
            ll.update({i: [0, value[i]]})

    for key, value in input_output_wire[1].items():
        ll = dict()
        x = None
        dict_of_inputs.update({key: x})
        dict_of_flatten_bits.update({key: ll})
        for i in range(value):
            value = re.search("(\d+'b)?(.*)",input_test_cases[key][index]).group(2)
            value = value[::-1]
            ll.update({i: [0, value[i]]})


    for key, value in input_output_wire[2].items():
        ll = dict()
        x = None
        dict_of_inputs.update({key: x})
        dict_of_flatten_bits.update({key: ll})
        for i in range(value):
            value = re.search("(\d+'b)?(.*)",input_test_cases[key][index]).group(2)
            value = value[::-1]
            ll.update({i: [0, value[i]]})



    for key, value in input_output_wire[3].items():
        ll = dict()
        x = None
        dict_of_inputs.update({key: x})
        dict_of_flatten_bits.update({key: ll})
        for i in range(value):
            value = re.search("(\d+'b)?(.*)",input_test_cases[key][index]).group(2)
            value = value[::-1]
            ll.update({i: [0, value[i]]})


    
    
    for i in range(1, num_of_test_cases):
        for key, value in dict_of_inputs.items():
            val = None
            if "'b" in input_test_cases[key][i]:
                val = re.search("\d+'b(.*)", input_test_cases[key][i]).group(1)
            else:
                val = input_test_cases[key][i]
            
            dict_of_inputs[key] = val

        for key, value in dict_of_inputs.items():
            last_dict = dict_of_flatten_bits[key]
            for index, bit in enumerate(reversed(value)):
                last_value = last_dict[index][1]
                counter = last_dict[index][0]
                if counter != 2 and last_value != bit:
                    last_dict[index][0] = counter+1
                    last_dict[index][1] = bit
   

    return dict_of_flatten_bits


def search_for_connection(node, nodeadj, G):
        edges = G.edges[node, nodeadj]["edge_attr"]
        return edges

def flip_output(Target_node, Graph, input_test_cases, index, curr_conn, curr_val):

    if isinstance(Target_node, INPUT):
        name_of_input = curr_conn.source.name
        list_of_inputs = list()
        curr = input_test_cases[name_of_input][-1]
        for bit in curr:
            list_of_inputs.append(bit)
        
        list_of_inputs[index] = curr_conn.PORT[0]
        
        input_test_cases[name_of_input][-1] = "".join(list_of_inputs)
       
         
    if isinstance(Target_node, bitwise):
        out_bit = None
        for conn in Target_node.connections:
            if Target_node == conn.source:
                out_bit = conn.PORT
        
        if Target_node.Type == "and" or Target_node.Type == "or":
            for conn in Target_node.connections:
                if Target_node == conn.destination:
                    conn.PORT = '1'

    elif isinstance(Target_node, OUTPUT):
        for conn in Target_node.connections:
            if Target_node == conn.destination:
                conn.PORT = str(int(not int(curr_val)))


       
    

    
    for parent in Graph.predecessors(Target_node):
        edges = search_for_connection(parent, Target_node, Graph)
        for edge in edges:
            if edge.destination_range == None:
                flip_output(parent, Graph, input_test_cases, index, edge, curr_val)
            elif index in edge.destination_range:
                flip_output(parent, Graph, input_test_cases, index, edge, curr_val)
        


def D_algorithm(input_test_cases, input_name,  index, curr_val, G):
    target_node = None
    for node in G.nodes():
        if isinstance(node, OUTPUT):
            if node.name == input_name:
                target_node = node
                break
    flip_output(target_node, G, input_test_cases, index, None, curr_val)
    
    





def Toggle_Coverage_Optimization(dict_of_flatten_bits, input_test_cases, input_output_wire, G, API, num_testcases):
    changed = True
    while(changed):
        changed = False
        for key, value in input_output_wire[0].items():
            input_test_cases[key].append(str())
        
        for key, value in dict_of_flatten_bits.items():
            if key not in input_output_wire[0]:
                continue
            for _, value2 in value.items():
                if value2[0] != 2:
                    changed = True
                    input_test_cases[key][-1] = str(int(not(int(value2[1])))) + input_test_cases[key][-1]
                    value2[1] = str(int(not(int(value2[1]))))
                    value2[0] += 1
                    
                

        for key, value in input_test_cases.items():
            for index, vec in enumerate(value):
                if len(vec) == 0:
                    value.remove(vec)
                    continue

                if "'b" not in vec:
                    value[index] = str(len(value[index])) + "'" + "b" + value[index]

        

    OUTPUTS = API.calc_output(input_test_cases)

    for key, value in OUTPUTS.items():
        num_testcases = len(value)
        input_test_cases[key] = value

    
    
    dict_of_flatten_bits = toggle_coverage(input_output_wire, input_test_cases, num_testcases, 0)

    changed = True
   
    for key, value in input_output_wire[0].items():
        IN = "".join([str(random.randint(0, 1)) for _ in range(value)])
        input_test_cases[key].append(IN)

    for key, value in dict_of_flatten_bits.items():
        if key not in input_output_wire[1]:
            continue
        for index, value2 in value.items():
            if value2[0] != 2:
                D_algorithm(input_test_cases, key, index, value2[1], G)
        

        

    
    



def append_all_conditions(G, node, parent_data):
    # Append the A data of the current node and its parents to the B attribute
    if node.cond is not None:
        node.all_conds.extend(node.cond + parent_data)
    
    # Recursively traverse children nodes
    for child in G.successors(node):
        if node.cond is not None:
            append_all_conditions(G, child, node.cond + parent_data)
        else:
            append_all_conditions(G, child, parent_data)    


def Collapse_SMT(conds, input_output_wire):
    list_of_conds = list() ## Anding the conditions for the SMT 
    solver = Solver()
    stack = list()
    dict_of_SMT = dict()
    for cond in conds:
        x = Generate_SMT_cond(cond[1], input_output_wire, dict_of_SMT)
        list_of_conds.append((x, cond[0]))



    if len(list_of_conds) != 1:
        stack.append(list_of_conds[0][0] == bool(int(list_of_conds[0][1])))
    else:
        stack.append(list_of_conds[0][0] == bool(int(list_of_conds[0][1])))

    list_of_conds.pop(0)
    for cond in list_of_conds:
        m = stack.pop()
        x = z3.And(cond[0] == bool(int(cond[1])), m)
        stack.append(x)
        pass


    return stack[-1]


    

        


    


def Branch_Coverage_Optimization(Branches_conditions, input_test_cases, input_output_wire, CODE_GRAPH, G, Blocks_and_Conditions, Testcases_Blocks_Coverage):
    root = get_root(G)
    for key, branch_cond in Branches_conditions.items():
        RHS = None
        solver = Solver()
        dict_of_new_inputs = dict()
        if int(branch_cond[0]) == 1:
            RHS = True
        elif int(branch_cond[0]) == 2:
            RHS = False
        else:
            continue
        Z3_EXPR = Collapse_SMT(branch_cond[1], input_output_wire)
        x = Z3_EXPR == RHS
        
        
        solver.add(Z3_EXPR == RHS)
        if solver.check() == sat:
            model = solver.model()
            for declaration in model.decls():
                var_name = declaration.name()
                var_value = None
                try:
                    var_value = bin(int(str(model[declaration])))[2:]
                except:
                    var_value = model[declaration]
                    if is_true(var_value):
                        var_value = '1'
                    else:
                        var_value = '0'
                dict_of_new_inputs.update({var_name: var_value})
                
        else:
            print("No solution found.") ##EDITTTT 
            

        statements_covered = []
        Insert_Random_Input(input_test_cases, input_output_wire[0], dict_of_new_inputs, CODE_GRAPH) 
        blocks_covered = 0
        print(Branches_conditions)
        blocks_covered, Branches_conditions, _ = traverse(root, -1,blocks_covered, Branches_conditions, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, statements_covered, explore = True, changed = True)
        blocks_covered -= 1 

        

        


def isUgate(Ast):
    return isinstance(Ast, Uand) or isinstance(Ast, Uor) or isinstance(Ast, Uxor) or isinstance(Ast, Uxor)


def parse_verilog_constant(verilog_const_str):
    # Split the string at the single quote character
    parts = verilog_const_str.split("'")
    if len(parts) == 1:
        return int(parts[0]) # since default in verilog is decimal
    elif len(parts) != 2:
        raise ValueError("Invalid Verilog constant format")

    # Extract the width and base
    width = int(parts[0])
    base = parts[1][0]

    # Extract the value
    value_str = parts[1][1:]
    if base == 'b':
        return int(value_str, 2)
    elif base == 'h':
        return int(value_str, 16)
    elif base == 'd':
        return int(value_str)
    else:
        return int(verilog_const_str)

# Function to evaluate a Pyverilog AST node representing a Verilog condition
def evaluate_condition(cond, comp, input_values, testcase_id):

    if isinstance(cond,Partselect):
        msb = int(cond.msb.value)
        lsb = int(cond.lsb.value)
        size = abs(msb - lsb) + 1
        input_string = input_values[str(cond.var)][testcase_id]
        reversed_msb = len(input_string) - 1 - msb
        reversed_lsb = len(input_string) - 1 - lsb
        new_Str = str(size) + "'b" + input_string[reversed_msb:reversed_lsb + 1]
        return parse_verilog_constant(new_Str)
    
    elif isinstance(cond,Pointer):
        bit = int(cond.ptr.value)
        input_string = input_values[str(cond.var)][testcase_id]
        new_bit = len(input_string) - 1 - bit
        new_Str = "1'b" + input_string[new_bit]
        return parse_verilog_constant(new_Str)

    elif isinstance(cond,Identifier):
        # Base case: Operand is an identifier (input variable)
        # Retrieve the value of the input variable from input_values dictionary
        
        return parse_verilog_constant(input_values[cond.name][testcase_id])

    elif isinstance(cond, IntConst):
        # Base case: Operand is an integer constant
        return parse_verilog_constant(cond.value)
    
    # Case statements
    elif isinstance(cond, tuple) and (len(cond) == 1):
        # Base case: Operand is an integer constant
        return parse_verilog_constant(input_values[comp][testcase_id]) == parse_verilog_constant(str(cond[0]))

    elif isinstance(cond, Operator): ## not always GT and Lor and Land
        # Recursive case: Operand is an operator node (e.g., GreaterThan, Eq, Lor, Land)
        # Evaluate the left and right sub-expressions recursively

        if isUgate(cond):
            x = evaluate_condition(cond.right,comp,input_values, testcase_id)
            size = int(re.search("(\d+)'.*", input_values[cond.right.name][0]).group(1))
            if isinstance(cond, Uand):
                if int((2**size) - 1) == int(x):
                    return True
                else:
                    return False
            if isinstance(cond, Uor):
                if int(x) > 0:
                    return True
                else:
                    return False
        else:
            left_result = evaluate_condition(cond.left,comp,input_values, testcase_id)
            right_result = evaluate_condition(cond.right,comp,input_values, testcase_id)

            

            # Perform the operation based on the operator type
            operator_type = cond.__class__.__name__
            if operator_type == 'GreaterThan':
                return left_result > right_result
            elif operator_type == 'GreaterEq':
                return left_result >= right_result
            elif operator_type == 'LessThan':
                return left_result < right_result
            elif operator_type == 'LessEq':
                return left_result <= right_result
            elif operator_type == 'Eq':
                return left_result == right_result
            elif operator_type == 'NotEq':
                return left_result != right_result
            elif operator_type == 'Land':
                return left_result and right_result
            elif operator_type == 'Lor':
                return left_result or right_result
            elif operator_type == 'LNot':
                return not right_result
            else:
                return False
        # Add more cases for other operators as needed


#input_test_cases = {'sel': 3}  # Input test case values

#---------------


def get_root(G):
    root = next(node for node, degree in G.in_degree() if degree == 0)
    return root




def generate_and_calculate_random_testcases(num_testcases, path, API):

   
    input_output_wire2, _ = get_input_output(path)
    input_output_wire = input_output_wire2.copy()
    for key, value in input_output_wire[0].items():
        input_output_wire[0][key] = int(value["msb"]) - int(value["lsb"]) + 1
    
    for key, value in input_output_wire[1].items():
        input_output_wire[1][key] = int(value["msb"]) - int(value["lsb"]) + 1

    for key, value in input_output_wire[2].items():
        input_output_wire[2][key] = int(value["msb"]) - int(value["lsb"]) + 1


    
    sizes = input_output_wire
    input_test_cases = random_stimuli(num_testcases, sizes) ## uncomment
    OUTPUTS_WIRE_DICT = API.calc_output(input_test_cases)
    for key, value in OUTPUTS_WIRE_DICT.items():
        input_test_cases.update({key: value})



    print(input_test_cases)
    return input_test_cases, input_output_wire



def traverse(node, testcase_id,blocks_covered, Dict_of_Branches, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, statements_covered, explore, changed = False ):
    # Evaluate the condition using the input test cases
        conditions = node.cond
        if node.cond is not None:
            final_result = True
            if explore:
                for condition in node.cond:
                    if len(condition) == 3:
                        result = evaluate_condition(condition[1],condition[2], input_test_cases, testcase_id)
                    else:
                        result = evaluate_condition(condition[1],None, input_test_cases, testcase_id)
                    if condition[0] == 0: # else statements so condition is inverted
                        result = not result
                    final_result = final_result and result
            else:
                final_result = False
        else:
            final_result = True # Block has no condition

        # Build Blocks_and_Conditions dict, it is testcase independent so do it only once
        if testcase_id == 0:
            changed = True
            Blocks_and_Conditions[node.block_id] = conditions
            if final_result: # always True
                Dict_of_Branches.update({node.block_id:(2, node.all_conds)}) 
            else: # always False
                Dict_of_Branches.update({node.block_id:(1, node.all_conds)}) 
        else:
            if node.block_id != 0 and Dict_of_Branches[node.block_id][0] == 2 and not final_result: #always true
                old_tup = Dict_of_Branches[node.block_id]
                new_tup = (3, old_tup[1])
                Dict_of_Branches[node.block_id] = new_tup
                changed = True

            elif node.block_id != 0 and Dict_of_Branches[node.block_id][0] == 1 and final_result:
                old_tup = Dict_of_Branches[node.block_id]
                new_tup = (3, old_tup[1])
                Dict_of_Branches[node.block_id] = new_tup
                changed = True
            

        print("Testcase: ", testcase_id," Block ID: ",node.block_id, " Condition result:", final_result,"\n")


        if final_result is True: # If the block is covered increment blocks covered and mark its statements as covered
            blocks_covered += 1
            statements_covered.extend(node.statements_list)

            # Dictionary were keys are testcases and values are list of blocks the testcase covers
            if testcase_id in Testcases_Blocks_Coverage:
                Testcases_Blocks_Coverage[testcase_id].append(node.block_id)
            else:
                Testcases_Blocks_Coverage[testcase_id] = [node.block_id]

            # Traverse children only if the final result is True
            for child in G.successors(node):
                blocks_covered,Dict_of_Branches, changed = traverse(child,testcase_id,blocks_covered,Dict_of_Branches, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, statements_covered, explore= True, changed = changed)
        else:
            for child in G.successors(node):
                blocks_covered, Dict_of_Branches, changed = traverse(child,testcase_id,blocks_covered,Dict_of_Branches, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, statements_covered, explore= False, changed = changed)

        
        # if testcase_id == 0:
        #     Dict_of_Branches.pop(0)
        #     #print("Dictionary of branches",Dict_of_Branches)
        #     total_blocks = len(Blocks_and_Conditions)-1
        #     #print("Total blocks = ", total_blocks)

        # percentage_covered = (blocks_covered / total_blocks) * 100 ## MALAK
        # print("Tescase ", testcase_id, " Blocks Covered ", blocks_covered, " Percentage block coverage", percentage_covered)
        # print("\n")
        # print(Testcases_Blocks_Coverage)
        # print("Statements Covered: ",statements_covered)
        return blocks_covered,Dict_of_Branches, changed
    
    
    

def remove_delay_control(file):
    # Read file
    with open("PARSER/files/" + file, 'r') as f:
        content = f.read()

    # Delay control regex pattern # then any number of digits then either ; or not followed by whitespaces
    pattern = r'#(\d+)(;?\s*)'

    # Substitute found matches with empty string
    modification = re.sub(pattern, '', content)

    # Write the modification to the given file
    with open(file, 'w') as f:
        f.write(modification)

def optimize_testset(input_test_cases, Testcases_Blocks_Coverage,unique_coverage,redundant_testcases):

    for key, value in Testcases_Blocks_Coverage.items():
        value_str = str(value)  # Convert the list to a string to use it as a hashable key
        if value_str in unique_coverage:
            # List of redundant testcases
            redundant_testcases.append(key)
            Testcases_Blocks_Coverage[key] = []  # Replace the value with an empty list
        else:
            unique_coverage[value_str] = key

# Call the function to plot the graph



def statistics(Dict_of_branches):
    num_of_branches = len(Dict_of_branches)
    numerator = 0
    for key, value in Dict_of_branches.items():
        if value[0] == 3 or value[0] == 2:
            numerator+=1

    return (numerator/num_of_branches) * 100


    
    


    


def all_toggled(dict_of_branches):
    for _, value in dict_of_branches.items():
        if value[0] != 3:
            return False
    return True
def COVERAGE_MAIN(path):
    # Remove delay control statements
    remove_delay_control(path)

    G = nx.DiGraph()  # Use DiGraph for directed graph
    assignments, always, _ = parse_verilog(path)

    # Create root node (this will not be counted as a block since it represents the module itself)
    root_block = My_Block(block_id=0)
    root_block.cond = None
    G.add_node(root_block)

    branch = 1

    # Handle always blocks
    for always_block in always: # 0 w 1...etc.
        x = parse_coverage_always(always_block.statement, G, branch, root_block)
        #root_block = parse_coverage_always(always[0].statement, G)
        if(x is not None):
            root_block.blocks_list.append(x)
            G.add_node(x)  # Add the block as a node in the graph
            G.add_edge(root_block,x)
    
    # if block coverage, we gather all assign statements in one block
    if(branch == 0):
        # Create assign block
        assign_block = My_Block(block_id=id)
        id+=1
        assign_block.cond = None
        G.add_node(assign_block)
        root_block.blocks_list.append(assign_block)
        G.add_edge(root_block,assign_block)

        for assign in assignments:
            assign_block.statements_list.append((str(assign.left.var) + '=' + str(assign.right.var),assign.lineno))
    # if branch coverage, node is only created if there is a condition.
    # Therefore, conitinuous assignment statements with no conditions are disregarded
    elif (branch == 1):
        # Handle assign statements
        for assign in assignments:
            try:
                # Code that might raise an exception
                assign.right.var.cond
            except Exception as e:
                # If there was no condition we disregard it
                pass
            else: # there is a condition
                # Code to execute if no exception occurs
                parse_assigns(assign.right.var,G,assign.left.var,root_block)
            finally:
                pass
                
    pos = nx.circular_layout(G)
    #pos = nx.shell_layout(G)

    nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=12)
    plt.show()

    Blocks_and_Conditions = {}
    Testcases_Blocks_Coverage = {}
    num_testcases = 5

    
    # Call random_stimuli function to initially generate random stimuli
    
    



    CODE_GRAPH, _ = code_to_graph(path)
    API = GraphAPI(CODE_GRAPH)


    input_test_cases, input_output_wire = generate_and_calculate_random_testcases(num_testcases, path, API)


    blocks_covered = 0
    Dict_of_Branches = dict()
    append_all_conditions(G, root_block, [])
    c = 0
    toggled = False
    n = 0
    while c != num_testcases:
        changed = None
        n+=1
        if n == 5:
            break
        blocks_covered, Dict_of_Branches, changed = traverse(root_block, c, blocks_covered, Dict_of_Branches, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, [], explore = True, changed = False)
        if c == 0: 
            Dict_of_Branches.pop(0)
        if not changed:
            input_test_cases2, _ = generate_and_calculate_random_testcases(1, path, API)
            for key, value in input_test_cases.items():
                value.remove(value[c])
                value.append(input_test_cases2[key][-1])
            blocks_covered, Dict_of_Branches, changed = traverse(root_block, c, blocks_covered, Dict_of_Branches, G, input_test_cases, Blocks_and_Conditions, Testcases_Blocks_Coverage, [], explore = True, changed = False)
            if changed:
                if all_toggled(Dict_of_Branches): 
                    toggled = True
                    break
                c+=1
        else:
            n = 0
            if all_toggled(Dict_of_Branches): 
                toggled = True
                break
            c+=1


     
    
    for key, value in input_test_cases.items():
        del value[c+1:]

    
    num_testcases = c+1
    dict_of_flatten_bits = toggle_coverage(input_output_wire, input_test_cases, num_testcases, 0)
    dict_of_flatten_bits_before = dict_of_flatten_bits.copy()
    Toggle_Coverage_Optimization(dict_of_flatten_bits, input_test_cases, input_output_wire, CODE_GRAPH, API, num_testcases) 
    

    SaveJson(dict_of_flatten_bits_before, dict_of_flatten_bits, "toggle")

    if not toggled:
        Branch_Coverage_Optimization(Dict_of_Branches, input_test_cases, input_output_wire, CODE_GRAPH, G, Blocks_and_Conditions, Testcases_Blocks_Coverage)


    print(input_test_cases)
    print(statistics(Dict_of_Branches))

    