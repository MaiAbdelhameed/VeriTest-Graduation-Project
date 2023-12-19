
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

from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import Assign, Concat, And, Xor, Partselect, Or, Xor, Pointer, Uand, IntConst, Uxor, Uor, Cond, Eq, Unot


import matplotlib.pyplot as plt
import re





def nodeingraph(G,a):
    for Nodeitr in G.nodes():

        if isinstance(a, gate): ## check if there is a gate with same size
            if a.Type != "not":
                if Nodeitr.size == a.size and isinstance(Nodeitr, gate):
                    input0 = Nodeitr.G[0]
                    input1 = Nodeitr.G[1]
                    if (a.G[0] == input0 or a.G[0] == input1) and (a.G[1] == input0 or a.G[1] == input1) and a.Type == Nodeitr.Type:
                        return Nodeitr
            else:
                if Nodeitr.size == a.size and isinstance(Nodeitr, gate) and a.Type == Nodeitr.Type:
                    input0 = Nodeitr.G[0]
                    if a.G[0] == input0:
                        return Nodeitr
        elif isinstance(a, UGate):
            if Nodeitr.size == a.size and isinstance(Nodeitr, UGate) and a.Type == Nodeitr.Type:
                    input0 = Nodeitr.G[0]
                    if a.G[0] == input0:
                        return Nodeitr




        
        else:
            if not isinstance(Nodeitr, UGate) and not isinstance(Nodeitr, mux) and not isinstance(Nodeitr, mGate) and not isinstance(Nodeitr, gate) and not isinstance(Nodeitr, ConstValue):
                if Nodeitr.name == a.name and Nodeitr.start == a.start and Nodeitr.end == a.end:
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
    ast.show()

    # Get all assignment statements from the AST
    assignments = get_assignments(ast)

    return assignments


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


def parse_assign_statement(assignment, input_output_wire, set_of_inputs, set_of_outputs, G, is_left):


    if isGate(assignment):
        right = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        left = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        G.add_node(left)
        G.add_node(right)
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
            INPUT_node.connect_input(Wire)
       
        else:
            Wire.connect_input(INPUT_node)
        return Wire
    
    if isinstance(assignment, Concat):
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
            INPUT_node.connect_input(Wire)
       
        else:
            Wire.connect_input(INPUT_node)
        G.add_edge(Wire, INPUT_node)
        return Wire
    
    if isinstance(assignment, IntConst):
        value = assignment.value
        fin_value = re.findall("\d+'\w(\d+)", value)
        Constant_node = ConstValue(Type = "ConstValue", size = len(fin_value[0]))
        Constant_node.connect_input(fin_value[0])
        return Constant_node
    
    
    if isinstance(assignment, Eq):
        selector_node = parse_assign_statement(assignment.left, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value = parse_assign_statement(assignment.right, input_output_wire, set_of_inputs, set_of_outputs, G, is_left)
        condition_value = condition_value.output[::-1]
        name_of_variable = selector_node.name
        and_gate = mGate(Type="Mand", Type_of_Mgate="Mand", size = 1)
        for i in range(0, len(condition_value), 1):
            wire_for_cond = wire(Type = "WIRE", size = 1, start = i, end = i, name= name_of_variable+ "_WIRE")
            node_itr = nodeingraph(G, wire_for_cond)
            if node_itr == None:
                wire_for_cond.connect_input(selector_node)
                G.add_edge(wire_for_cond, selector_node)

            else:
                wire_for_cond = node_itr

            if condition_value[i] == "0":
                not_gate = gate(Type = "not", Type_of_gate="not", size = 1)
                not_gate.connect_input(wire_for_cond)
                node_itr = nodeingraph(G, not_gate)
                if node_itr == None:
                    and_gate.connect_input(not_gate)
                    G.add_edge(not_gate, and_gate)
                    G.add_edge(not_gate, wire_for_cond)
                else:
                    and_gate.connect_input(node_itr)
                    G.add_edge(node_itr, and_gate)
                    


            else:
                and_gate.connect_input(wire_for_cond)
                G.add_edge(wire_for_cond, and_gate)


        return and_gate
        
           



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

    

    

        

def parse_verilog_code():
    verilog_file = "module.v"
    assignments = parse_verilog(verilog_file)
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

    
    
    set_of_inputs = set()
    set_of_outputs = set()



    # Print the assignment statements
    for assignment in assignments:
        final_output = parse_assign_statement(assignment.right.var, input_output_wire, set_of_inputs, set_of_outputs, G, False)
        output_port = parse_assign_statement(assignment.left.var, input_output_wire, set_of_inputs, set_of_outputs, G, True)
        output_port.connect_input(final_output)
        G.add_edge(final_output, output_port)
        


    return G, set_of_inputs, set_of_outputs



   



    





