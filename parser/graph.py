
import networkx as nx
from components.Gate import gate
from components.INPUT import INPUT
from components.Ugate import UGate
from components.MGate import mGate

from components.Wire import wire
from components.output import OUTPUT
from components.MUX import mux
from components.ConstValue import ConstValue
from preprocessing.find import *
from components.condgate import condgate

from components.dontcares import dontcares

from pyverilog.vparser.parser import parse
#from pyverilog.vparser.ast import Assign, Concat, And, Xor, Partselect, Or, Xor, Pointer, Uand, IntConst, Uxor, Uor, Cond, Eq, Unot,Always, GreaterThan, LessThan, LessEq, GreaterEq, NotEq, IfStatement
from pyverilog.vparser.ast import *

import matplotlib.pyplot as plt
import re





def nodeingraph(G,a):
    type_of_node = type(a)
    # print(type_of_node)
    for Nodeitr in G.nodes():
        if type_of_node != type(Nodeitr):
            continue
        if isinstance(Nodeitr, gate): ## check if there is a gate with same size
            if a.Type != "not" and Nodeitr.Type != "not":
                if Nodeitr.size == a.size:
                    input0 = Nodeitr.G[0]
                    input1 = Nodeitr.G[1]
                    if (a.G[0] == input0 or a.G[0] == input1) and (a.G[1] == input0 or a.G[1] == input1) and a.Type == Nodeitr.Type:
                        return Nodeitr
            elif a.Type == "not" and Nodeitr.Type == "not":
                if Nodeitr.size == a.size:
                    input0 = Nodeitr.G[0]
                    if a.G[0] == input0:
                        return Nodeitr
        elif isinstance(Nodeitr, UGate):
            if Nodeitr.size == a.size:
                input0 = Nodeitr.G[0]
                if a.G[0] == input0:
                    return Nodeitr

        
        elif isinstance(Nodeitr, INPUT) or isinstance(Nodeitr, OUTPUT):
            if Nodeitr.name == a.name and Nodeitr.start == a.start and Nodeitr.end == a.end:
                return Nodeitr
    return None


def get_always_block(node):
    always_blocks = []
    if isinstance(node, Always):
        always_blocks.append(node)

    # Recursively visit child nodes
    for child in node.children():
        always_blocks.extend(get_always_block(child))

    return always_blocks






def get_assignments(node):
    assignments = []

    if isinstance(node, Assign):
        # Add the assignment to the list
        assignments.append(node)

    # Recursively visit child nodes
    for child in node.children():
        assignments.extend(get_assignments(child))

    return assignments

def parse_verilog(file_path):
    # Parse the Verilog code
    ast, _ = parse([file_path])
    ast.show()

    # Get all assignment statements from the AST
    assignments = get_assignments(ast)
    always_blocks = get_always_block(ast)

    return assignments, always_blocks


def isGate(right):
    return isinstance(right, And) or isinstance(right, Or) or isinstance(right, Xor)

def isUGate(right):
    return isinstance(right, Uand) or isinstance(right, Uor) or isinstance(right, Uxor) or isinstance(right, Unot)


def gatetype(right):
    if isinstance(right, And):
        return "and"
    elif isinstance(right, Or):
        return "or"
    elif isinstance(right, Xor):
        return "xor"
    
def Ugatetype(right):
    if isinstance(right, Uand):
        return "Uand"
    elif isinstance(right, Uor):
        return "Uor"
    elif isinstance(right, Uor):
        return "Uxor"
    elif isinstance(right, Unot):
        return "Unot"
    
def hasFalsevalue(statement, list_of_false_statments):
    if isinstance(statement, tuple):
        for false_statement in list_of_false_statments:
            if type(false_statement) == tuple:
                if statement[0] == false_statement[0]:
                    return false_statement
            elif isinstance(false_statement, mux):
                if statement[0] == false_statement.bind:
                    return false_statement
    else:
        for false_statement in list_of_false_statments:
            if type(false_statement) == tuple:
                if statement.bind == false_statement[0]:
                    return false_statement
            elif isinstance(false_statement, mux):
                if statement.bind == false_statement.bind:
                    return false_statement

    return None


def parse_always_block(always, input_output_wire, set_of_inputs, set_of_outputs, G):
    if (always == None):
        return always

    if isinstance(always, Block):
        list_of_statements = list() ## list of tuples
        for statement in always.statements: ## rag3 b3d el for loop
            
            x = parse_always_block(statement, input_output_wire, set_of_inputs, set_of_outputs, G)
            if type(x) == tuple:
                list_of_statements.append(x)
            else:
                list_of_statements.extend(x)
        return list_of_statements
            
    elif isinstance(always, IfStatement):
        list_of_true_statments = list()
        list_of_false_statments = list()
        true = parse_always_block(always.true_statement, input_output_wire, set_of_inputs, set_of_outputs, G)
        false = parse_always_block(always.false_statement, input_output_wire, set_of_inputs, set_of_outputs, G)
        if false != None:
            if type(false) == tuple:
                list_of_false_statments.append(false)
            else:
                list_of_false_statments.extend(false)
        if type(true) == tuple:
            list_of_true_statments.append(true)
        else:
            list_of_true_statments.extend(true)

        list_of_IF_statements = list()
        for statement in list_of_true_statments:
            false_statement = hasFalsevalue(statement, list_of_false_statments)
            if false_statement != None:
                list_of_false_statments.remove(false_statement)
            true_node = None
            size = 0
            bind = None
            if type(statement) == tuple:
                true_node = statement[1]
                size = statement[1].size
                bind = statement[0]
            else:
                true_node = statement
                size = statement.size
                bind = statement.bind
            if type(false_statement) == tuple:
                sel = parse_always_block(always.cond, input_output_wire, set_of_inputs, set_of_outputs, G)
                mux2x1 = mux(Type = "MUX", size = false_statement[1].size, start = 0, end = false_statement[1].size-1)
                mux2x1.connect_input(true_node)
                G.add_edge(mux2x1, true_node)
                mux2x1.connect_input(false_statement[1])
                G.add_edge(mux2x1,false_statement[1])
                mux2x1.bind = bind
                mux2x1.connect_selector(sel)
                G.add_edge(mux2x1, sel)
                list_of_IF_statements.append(mux2x1)
            elif isinstance(false_statement,mux):
                sel = parse_always_block(always.cond, input_output_wire, set_of_inputs, set_of_outputs, G)
                mux2x1 = mux(Type = "MUX", size = size, start = 0, end = size-1)                
                mux2x1.connect_input(true_node)
                G.add_edge(mux2x1, true_node)
                mux2x1.connect_input(false_statement)
                G.add_edge(mux2x1, false_statement)
                mux2x1.bind = bind
                G.add_edge(mux2x1, sel)
                list_of_IF_statements.append(mux2x1)
            else: ## connect dont care
                dontcare_node = dontcares(size=size)
                sel = parse_always_block(always.cond, input_output_wire, set_of_inputs, set_of_outputs, G)
                mux2x1 = mux(Type = "MUX", size = size, start = 0, end = size-1)                
                mux2x1.connect_input(true_node)
                G.add_edge(mux2x1, true_node)
                mux2x1.connect_input(dontcare_node)
                G.add_edge(mux2x1, dontcare_node)
                G.add_edge(mux2x1, sel)
                mux2x1.bind = bind
                list_of_IF_statements.append(mux2x1)

        for statement in list_of_false_statments:
            dontcare_node = dontcares(size=statement[0].size)
            if type(statement) == tuple:
                sel = parse_always_block(always.cond, input_output_wire, set_of_inputs, set_of_outputs, G)
                mux2x1 = mux(Type = "MUX", size = size, start = 0, end = size-1)                
                mux2x1.connect_input(dontcare_node)
                G.add_edge(mux2x1, dontcare_node)
                mux2x1.connect_input(statement[1])
                G.add_edge(mux2x1, statement[1])
                G.add_edge(mux2x1, sel)
                mux2x1.bind = statement[0]
                list_of_IF_statements.append(mux2x1)
            else:
                pass



              
       

                


                
        

        return list_of_IF_statements

        
        
    elif isinstance(always, IntConst): ## missing
        value = always.value
        fin_value = re.findall("\d+'\w(\d+)", value)
        Constant_node = ConstValue(Type = "ConstValue", size = len(fin_value[0]))
        Constant_node.connect_input(fin_value[0])
        set_of_inputs.add(Constant_node)
        return Constant_node
    

    elif isinstance(always, LessEq):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "le","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate

    elif isinstance(always, GreaterEq):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "ge","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    elif isinstance(always, NotEq):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "ne","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    elif isinstance(always, LessThan):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "lt","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate

    elif isinstance(always, GreaterThan):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "gt","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    
    elif isinstance(always, Eq):
        selector_node = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        condition_value_node = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "eq","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate

    elif isinstance(always, NonblockingSubstitution):
        left = parse_always_block(always.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        right = parse_always_block(always.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        tup = (left, right)
        return tup
    
    elif isinstance(always, Lvalue) or isinstance(always, Rvalue):
        return parse_always_block(always.var, input_output_wire, set_of_inputs, set_of_outputs, G)
    
    else:
        name_of_variable = always.name
        search_for_input = None
        Type = None
        size = None
        if name_of_variable in input_output_wire[0]:
            Type = "INPUT"
            size = input_output_wire[0][name_of_variable]
            search_for_input = INPUT(Type="INPUT", size = size, start=0, end=size-1, name=name_of_variable)
            
        elif name_of_variable in input_output_wire[2]:
            Type = "WIRE"
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", size = size, start=0, end=size-1, name=name_of_variable)
        
        elif name_of_variable in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", size = size, start=0, end=size-1, name=name_of_variable)
            

        node_itr = nodeingraph(G, search_for_input)
        if node_itr == None: 
            if Type == "INPUT":
                set_of_inputs.add(search_for_input)
            elif Type == "OUTPUT":
                set_of_outputs.add(search_for_input)
            G.add_node(search_for_input)
            return search_for_input
                
        else:
            return node_itr



    


    

def parse_assign_statement(assignment, input_output_wire, set_of_inputs, set_of_outputs, G, is_left):


    if isGate(assignment):
        right = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        left = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        Type = gatetype(assignment)
        Gate = gate(Type=Type, Type_of_gate = Type, size = left.size)
        Gate.connect_input(right)
        Gate.connect_input(left)
        node_itr = nodeingraph(G, Gate)
        if node_itr == None:
            G.add_edge(Gate,right)
            G.add_edge(Gate,left)

        else:
            return node_itr


        return Gate
    
    if isinstance(assignment, Partselect):
        INPUT_node = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = INPUT_node.name
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        size = abs(msb-lsb) 
        Wire = wire(Type = "WIRE", size = size+1, start = lsb, end = msb, name= name_of_variable+ "_WIRE")
        nodeitr = nodeingraph(G, Wire)
        if nodeitr != None:
            return nodeitr
        G.add_edge(Wire, INPUT_node)

        if is_left:
            if isinstance(INPUT_node, wire):
                INPUT_node.isleft = True
            INPUT_node.connect_input(Wire)
       
        else:
            Wire.connect_input(INPUT_node)
        return Wire
    
    if isinstance(assignment, Concat): ## Missing: check if concat gate exist
        list_of_concat_element = list()
        size = 0
        Gate = gate(Type = "concat", Type_of_gate= "concat", size=size)
        for element in assignment.list:
            node = parse_assign_statement(element, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
            size += node.size
            list_of_concat_element.append(node)
            Gate.connect_input(node)
            G.add_edge(Gate, node)

        Gate.size = size

        return Gate
    
    if isinstance(assignment, Cond):
        input1 = parse_assign_statement(assignment.false_value, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        input0 = parse_assign_statement(assignment.true_value, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        sel = parse_assign_statement(assignment.cond, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        mux2x1 = mux(Type = "MUX", size = input0.size, start = 0, end = input0.size-1)
        mux2x1.connect_input(input0)
        mux2x1.connect_input(input1)
        mux2x1.connect_selector(sel)
        G.add_edge(mux2x1, input0)
        G.add_edge(mux2x1, input1)
        G.add_edge(mux2x1, sel)
        return mux2x1




    
    if isinstance(assignment, Pointer):
        INPUT_node = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = INPUT_node.name
        value = int(assignment.ptr.value)
        Wire = wire(Type = "WIRE", size = 1, start = value, end = value, name= name_of_variable+ "_WIRE")
        nodeitr = nodeingraph(G, Wire)
        if nodeitr != None:
            return nodeitr
        
        if is_left:
            if isinstance(INPUT_node, wire):
                INPUT_node.isleft = True
            INPUT_node.connect_input(Wire)
       
        else:
            Wire.connect_input(INPUT_node)
        G.add_edge(Wire, INPUT_node)
        return Wire
    
    if isinstance(assignment, IntConst): ## missing
        value = assignment.value
        fin_value = re.findall("\d+'\w(\d+)", value)
        Constant_node = ConstValue(Type = "ConstValue", size = len(fin_value[0]))
        Constant_node.connect_input(fin_value[0])
        set_of_inputs.add(Constant_node)
        return Constant_node
    

    if isinstance(assignment, LessEq):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "le","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate

    if isinstance(assignment, GreaterEq):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "ge","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    if isinstance(assignment, NotEq):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "ne","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    if isinstance(assignment, LessThan):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "lt","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate

    if isinstance(assignment, GreaterThan):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "gt","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
    
    
    if isinstance(assignment, Eq):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        name_of_variable = selector_node.name
        tup = (selector_node, condition_value_node, "eq","none")
        condition_gate = condgate(tup)
        G.add_edge(condition_gate, selector_node)
        G.add_edge(condition_gate, condition_value_node)
        condition_gate.connect_input(condition_value_node)
        condition_gate.connect_input(selector_node)
        return condition_gate
        
    

    if isUGate(assignment):
        Type = Ugatetype(assignment)
        if Type != "Unot":
            INPUT_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
            name_of_variable = INPUT_node.name
            size = 1
            Single_input_Gate = UGate(Type = Type, Type_of_Ugate = Type, size = size)
            Single_input_Gate.connect_input(INPUT_node)
            node_itr = nodeingraph(G, Single_input_Gate)
            if node_itr == None:
                G.add_edge(Single_input_Gate, INPUT_node)
                return Single_input_Gate
            else:
                return node_itr
        elif Type == "Unot":
            INPUT_node = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
            name_of_variable = INPUT_node.name
            size = INPUT_node.size
            Single_input_Gate = gate(Type = "not", Type_of_gate= "not", size = size)
            Single_input_Gate.connect_input(INPUT_node)
            node_itr = nodeingraph(G, Single_input_Gate)
            if node_itr == None:
                G.add_edge(Single_input_Gate, INPUT_node)
                return Single_input_Gate
            else:
                return node_itr



        


        
    
    else: 
        name_of_variable = assignment.name
        search_for_input = None
        Type = None
        size = None
        if name_of_variable in input_output_wire[0]:
            Type = "INPUT"
            size = input_output_wire[0][name_of_variable]
            search_for_input = INPUT(Type="INPUT", size = size, start=0, end=size-1, name=name_of_variable)
            
        elif name_of_variable in input_output_wire[2]:
            Type = "WIRE"
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", size = size, start=0, end=size-1, name=name_of_variable)
        
        elif name_of_variable in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", size = size, start=0, end=size-1, name=name_of_variable)
            

        node_itr = nodeingraph(G, search_for_input)
        if node_itr == None: ## INPUT not in Graph
            if Type == "INPUT":
                set_of_inputs.add(search_for_input)
            elif Type == "OUTPUT":
                set_of_outputs.add(search_for_input)

            return search_for_input
                
        else:
            return node_itr

    

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

        

def parse_verilog_code():
    verilog_file = "module.v"
    assignments, always_blocks = parse_verilog(verilog_file)
    G = nx.Graph()
    file = open(verilog_file)
    input_output_wire2 = get_input_output()
    input_output_wire = input_output_wire2.copy()
    for key, value in input_output_wire[0].items():
        input_output_wire[0][key] = int(value["msb"]) - int(value["lsb"]) + 1
    
    for key, value in input_output_wire[1].items():
        input_output_wire[1][key] = int(value["msb"]) - int(value["lsb"]) + 1

    for key, value in input_output_wire[2].items():
        input_output_wire[2][key] = int(value["msb"]) - int(value["lsb"]) + 1


    print(input_output_wire)
    
    
    set_of_inputs = set()
    set_of_outputs = set()



    # Print the assignment statements
    for assignment in assignments:
        final_output = parse_assign_statement(assignment.right.var, input_output_wire, set_of_inputs, set_of_outputs, G, False)
        output_port = parse_assign_statement(assignment.left.var, input_output_wire, set_of_inputs, set_of_outputs, G, True)

        output_port.connect_input(final_output)
        G.add_edge(final_output, output_port)
        


    


    for always in always_blocks:
        x = parse_always_block(always.statement, input_output_wire, set_of_inputs, set_of_outputs, G)
        for component in x:
            if isinstance(component, mux):
                component.bind.connect_input(component)
                G.add_edge(component.bind, component)
        

    return G, set_of_inputs, set_of_outputs



   



    





