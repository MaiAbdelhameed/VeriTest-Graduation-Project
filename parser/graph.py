
import networkx as nx
from components.Gate import gate
from components.INPUT import Input

from components.Wire import wire
from components.OUTPUT import Output

from preprocessing.find import *
import matplotlib.pyplot as plt
import re
from Token import *
from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import Assign, Concat, And, Xor, Variable, Value, Partselect, Or, Xor, Pointer
from components.INPUT import Input
import networkx as nx
import matplotlib.pyplot as plt





def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if not isinstance(Nodeitr, gate):
            if Nodeitr.name == a:
                return Nodeitr
    return None




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
    # ast.show()

    # Get all assignment statements from the AST
    assignments = get_assignments(ast)

    return assignments


def isGate(right):
    return isinstance(right, And) or isinstance(right, Or) or isinstance(right, Xor)


def gatetype(right):
    if isinstance(right, And):
        return "and"
    elif isinstance(right, Or):
        return "or"
    elif isinstance(right, Xor):
        return "xor"


def parse_assign_statement(assignment, input_output_wire, set_of_inputs, set_of_outputs, G):


    if isGate(assignment):
        right = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G)
        left = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G)
        G.add_node(left)
        G.add_node(right)
        Type = gatetype(assignment)
        Gate = gate(Type=Type, Type_of_gate = Type, size = left.size)
        Gate.connect_input(right)
        Gate.connect_input(left)
        G.add_edge(Gate,right)
        G.add_edge(Gate,left)
        return Gate
    
    if isinstance(assignment, Partselect):
        Input_node = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = Input_node.name
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        size = abs(msb-lsb)
        Wire = wire(Type = "WIRE", size = size + 1, start = lsb, end = msb, name= name_of_variable+ "_WIRE")
        G.add_edge(Wire, Input_node)
        Wire.connect_input(Input_node)
        return Wire
    
    if isinstance(assignment, Concat):
        list_of_concat_element = list()
        size = 0
        Gate = gate(Type = "concat", Type_of_gate= "concat", size=size)
        for element in assignment.list:
            node = parse_assign_statement(element, input_output_wire, set_of_inputs, set_of_outputs, G)
            size += node.size
            list_of_concat_element.append(node)
            Gate.connect_input(node)
            G.add_edge(Gate, node)

        Gate.size = size

        return Gate
    
    if isinstance(assignment, Pointer):
        Input_node = parse_assign_statement(assignment.var, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_variable = Input_node.name
        value = int(assignment.ptr.value)
        Wire = wire(Type = "WIRE", size = 1, start = value, end = value, name= name_of_variable+ "_WIRE")
        G.add_edge(Wire, Input_node)
        Wire.connect_input(Input_node)
        return Wire



        
    
    else: 
        name_of_variable = assignment.name
        node_itr = nodeingraph(G, name_of_variable)
        if node_itr == None: ## Input not in Graph
            Type = None
            if name_of_variable in input_output_wire[0]:
                Type = "INPUT"
                size = input_output_wire[0][name_of_variable]
            else:
                Type = "WIRE"
                size = input_output_wire[2][name_of_variable]

            if Type == "INPUT":
                input_node = Input(Type="INPUT", size = size, start=0, end=size-1, name=name_of_variable)
                set_of_inputs.add(input_node)
                return input_node
            else:
                wire_node = wire(Type="WIRE", size = size, start=0, end=size-1, name=name_of_variable)
                return wire_node
        else:
            return node_itr

    

    

        

def parse_verilog_code():
    verilog_file = "module.v"
    assignments = parse_verilog(verilog_file)
    G = nx.Graph()
    file = open(verilog_file)
    input_output_wire = get_input_output(file)
    dictionary = input_output_wire[0]
    values = dictionary.values()
    input_output_wire = next(iter(values))
    set_of_inputs = set()
    set_of_outputs = set()



    # Print the assignment statements
    for assignment in assignments:
        final_output = parse_assign_statement(assignment.right.var, input_output_wire, set_of_inputs, set_of_outputs, G)
        name_of_output = assignment.left.var.name
        print(input_output_wire)
        Type = None
        if name_of_output in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_output]
        else:
            Type = "WIRE"
            size = input_output_wire[2][name_of_output]
        

        if Type == "OUTPUT":
            out = Output(Type=Type, size=size, start = 0, end = size-1, name = name_of_output)
        else:
            out = wire(Type=Type, size=size, start = 0, end = size-1, name = name_of_output)

        out.connect_input(final_output)
        G.add_edge(final_output, out)
        set_of_outputs.add(out)


    return G, set_of_inputs, set_of_outputs



   



    





