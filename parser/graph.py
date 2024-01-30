
import networkx as nx
from components.GATE import gate
from components.INPUT import INPUT
from components.Ugate import UGate


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
from connection import connection

import matplotlib.pyplot as plt
import re





def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if isinstance(Nodeitr, INPUT) or isinstance(Nodeitr, OUTPUT) or isinstance(Nodeitr, wire):
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
                mux2x1 = mux(Type = "MUX")
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
                mux2x1 = mux(Type = "MUX")               
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
                mux2x1 = mux(Type = "MUX")               
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
                mux2x1 = mux(Type = "MUX")             
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
        Constant_node = ConstValue(CONST = fin_value[0])
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

def create_out_connection(assignment, input_output_wire, set_of_inputs, set_of_outputs, G, is_left):

    if isinstance(assignment, Partselect):
        connecting_edge = create_out_connection(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        connecting_edge.destination_range = (lsb, msb)
        return connecting_edge
    elif isinstance(assignment, Pointer):
        connecting_edge = create_out_connection(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        value = int(assignment.ptr.value)
        connecting_edge.destination_range = (value, value)
        return connecting_edge
    
    else: 
        name_of_variable = assignment.name
        search_for_input = None
        size = None
        connecting_edge = connection()


        if name_of_variable in input_output_wire[1]:

            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", size = size, start=0, end=size-1, name=name_of_variable)
            
        else:
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", size = size, start=0, end=size-1, name=name_of_variable)
        

        node_itr = nodeingraph(G, search_for_input)
        if node_itr == None: 
            search_for_input.add_connection(connecting_edge)
            connecting_edge.destination = search_for_input
            return connecting_edge
                
        else:
            node_itr.add_connection(connecting_edge)
            connecting_edge.destination = node_itr
            return connecting_edge
    


def create_connection(gate, connection, G, isTrueValue = False, isFalseValue = False, isSelector = False):
    connection.destination = gate
    connection.isTrueValue = isTrueValue
    connection.isFalseValue = isFalseValue
    connection.isinstance = isSelector
    gate.add_connection(connection)
    G.add_edge(connection.source, gate, edge_attr=connection)



def create_condition(condition, lhs_value_node_connection, rhs_value_node_connection, G):
    condition_gate = condgate(condition)
    create_connection(condition_gate, lhs_value_node_connection, G)
    create_connection(condition_gate, rhs_value_node_connection, G)
    condition_gate_connecting_edge = connection()
    condition_gate_connecting_edge.source = condition_gate
    condition_gate.add_connection(condition_gate_connecting_edge)
    return condition_gate_connecting_edge


def parse_assign_statement(assignment, input_output_wire, set_of_inputs, set_of_outputs, G, is_left):

    if isGate(assignment):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        Type = gatetype(assignment)
        Gate = gate(Type=Type, Type_of_gate = Type, size = right_connection.source.size)
        create_connection(Gate, right_connection, G)
        create_connection(Gate, left_connection, G)
        connecting_edge = connection()
        Gate.add_connection(connecting_edge)
        connecting_edge.source = Gate
        return connecting_edge
    
    if isinstance(assignment, Partselect):
        connecting_edge = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        connecting_edge.source_range = (lsb, msb)
        return connecting_edge
    
    if isinstance(assignment, Concat): ## Missing: check if concat gate exist
        size = 0
        concat_gate = gate(Type = "concat", Type_of_gate= "concat", size=size)
        for element in assignment.list:
            concat_element_connection = parse_assign_statement(element, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
            size += concat_element_connection.source.size
            create_connection(concat_gate, concat_element_connection, G)

        
        concat_gate.size = size
        concat_gate_connection = connection()
        concat_gate_connection.source = concat_gate

        return concat_gate_connection
    
    if isinstance(assignment, Cond):
        true_value_connection = parse_assign_statement(assignment.false_value, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        false_value_connection = parse_assign_statement(assignment.true_value, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        sel_connection = parse_assign_statement(assignment.cond, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        ## in case that the sel_edge source was an Input, in this case
        ## we will first connect the input to a condition gate to compare it with 1's
        if isinstance(sel_connection.source, INPUT): 
            condition_gate_connection = connection()
            condition_gate = condgate("eq")
            create_connection(condition_gate, sel_connection, G)
            condition_gate_connection.source = condition_gate
            condition_gate.add_connection(condition_gate_connection)
            sel_connection = condition_gate_connection
        
        mux2x1 = mux(Type = "MUX")
        create_connection(mux2x1, true_value_connection, G, isTrueValue=True)
        create_connection(mux2x1, false_value_connection, G, isFalseValue=True)
        create_connection(mux2x1, sel_connection, G, isSelector=True)
        connecting_edge = connection()
        connecting_edge.source = mux2x1
        mux2x1.add_connection(connecting_edge)
        return connecting_edge


    
    if isinstance(assignment, Pointer):
        connecting_edge = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        value = int(assignment.ptr.value)
        connecting_edge.source_range = (value, value)
        return connecting_edge

    
    if isinstance(assignment, IntConst): ## missing
        value = assignment.value
        fin_value = re.findall("\d+'\w(\d+)", value)
        connecting_edge = connection()
        Constant_node = ConstValue(CONST = fin_value[0])
        connecting_edge.source = Constant_node
        Constant_node.add_connection(connecting_edge)
        G.add_node(Constant_node)
        return connecting_edge
    

    if isinstance(assignment, LessEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("le", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(assignment, GreaterEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("ge", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    if isinstance(assignment, NotEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("ne", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
        
    
    if isinstance(assignment, LessThan):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("lt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(assignment, GreaterThan):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("gt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    
    if isinstance(assignment, Eq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_gate_connecting_edge = create_condition("eq", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
        
    

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
        connecting_edge = connection()

        ## SEARCH FOR INPUT OR OUTPUT OR WIRE ##
        if name_of_variable in input_output_wire[0]: 
            Type = "INPUT"
            size = input_output_wire[0][name_of_variable]
            search_for_input = INPUT(Type="INPUT", size = size, start=0, end=size-1, name=name_of_variable)

        elif name_of_variable in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", size = size, start=0, end=size-1, name=name_of_variable)
            
        elif name_of_variable in input_output_wire[2]:
            Type = "WIRE"
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", size = size, start=0, end=size-1, name=name_of_variable)
        


        node_itr = nodeingraph(G, search_for_input)
        if node_itr == None: ## INPUT not in Graph
            if Type == "INPUT":
                set_of_inputs.add(search_for_input)
            elif Type == "OUTPUT":
                set_of_outputs.add(search_for_input)

            G.add_node(search_for_input)
            
            connecting_edge.source = search_for_input
            search_for_input.add_connection(connecting_edge)
            return connecting_edge
                
        else:
            
            connecting_edge.source = node_itr
            node_itr.add_connection(connecting_edge)
            return connecting_edge

    
def merge_connections(connection1, connection2):
    if connection1.source == None:
        connection1.source = connection2.source
        connection1.source_range = connection2.source_range

    else:
        connection1.destination = connection2.destination
        connection1.destination_range = connection2.destination_range

    return connection1

    

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

        

def parse_verilog_code():
    verilog_file = "module.v"
    assignments, always_blocks = parse_verilog(verilog_file)
    G = nx.DiGraph()
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
        final_output_connection = parse_assign_statement(assignment.right.var, input_output_wire, set_of_inputs, set_of_outputs, G, False)
        output_port_connection = create_out_connection(assignment.left.var, input_output_wire, set_of_inputs, set_of_outputs, G, True)
        connection = merge_connections(final_output_connection, output_port_connection)
        G.add_edge(connection.source, connection.destination, edge_attr = connection)

        # output_port.connect_input(final_output)
        # G.add_edge(final_output, output_port)
        


    


    for always in always_blocks:
        x = parse_always_block(always.statement, input_output_wire, set_of_inputs, set_of_outputs, G)
        for component in x:
            if isinstance(component, mux):
                component.bind.connect_input(component)
                G.add_edge(component.bind, component)
        

    return G, set_of_inputs, set_of_outputs







    





