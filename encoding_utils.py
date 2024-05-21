# from Coverage.coverage import COVERAGE_MAIN
from PARSER.Simulate import PRASER_MAIN
from PARSER.GraphAPI import GraphAPI
from PARSER.code_to_graph import code_to_graph
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.connection import connection
####################################
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
####################################
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
####################################
from PARSER.components.IN_OUT_WIRE.REG import REG
####################################
from PARSER.components.Gates.ConstValue import ConstValue
####################################
# arithmetic
from PARSER.components.Gates.adder import adder
from PARSER.components.Gates.subtractor import subtractor
from PARSER.components.Gates.multplyer import multplyer
from PARSER.components.Gates.shift import shift
from PARSER.components.Gates.power import power

# conditional
from PARSER.components.Gates.condgate import condgate
from PARSER.components.Gates.MUX import mux

# bitwise
from PARSER.components.Gates.Ugate import UGate
from PARSER.components.Gates.bitwise import bitwise
from PARSER.components.Gates.Lgate import Lgate

# case
from PARSER.components.Gates.Case import Case

# concatenation
from PARSER.components.Gates.concatenation import concatenation

##############################################
# for node sizes
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.connection import connection
import re


# type => input 0, output 1, reg 2, operation 3, constValue 4
# type_operation=> arthimatic 1, condition 2, logical/bitwise gate operators 3, case 4
# number of connections
# size of node
"""
arithmetic => + - * ** , left shift, right shift
conditional => == != >= <= > <
logical/bitwise operators => &, |, xor, nand,...etc (any gates)
case
concatenation
"""
type_index = {
    "input": "1000",
    "output": "0100",
    "reg": "0010",
    "wire": "0001",
    "operation" : "0000"
}

# operation_index = {
#     "no_operation": 0,
#     "arithmetic": 1,
#     "condition": 2,
#     "bitwise": 3,
#     "case": 4,
#     "concatenation": 5
# }

operation_index = {
    "nop":          "0000",
    "not":			"1000",
    "or":			"0100",
    "and":			"0010",
    "constVal":     "0001"
}


def get_encoding(node):
    result = []
    # input type
    if (isinstance(node, INPUT)):
        temp = [int(char) for char in type_index["input"]]
        result.extend(temp)
        temp = [int(char) for char in operation_index["nop"]]
        result.extend(temp)
    # output type
    elif (isinstance(node, OUTPUT)):
        temp = [int(char) for char in type_index["output"]]
        result.extend(temp)
        temp = [int(char) for char in operation_index["nop"]]
        result.extend(temp)
    # reg type
    elif (isinstance(node, REG)):
        temp = [int(char) for char in type_index["reg"]]
        result.extend(temp)
        temp = [int(char) for char in operation_index["nop"]]
        result.extend(temp)
    # wire type
    elif (isinstance(node, wire)):
        temp = [int(char) for char in type_index["wire"]]
        result.extend(temp)
        temp = [int(char) for char in operation_index["nop"]]
        result.extend(temp)
        
    elif (isinstance(node, ConstValue)):
        temp = [int(char) for char in type_index["operation"]]
        result.extend(temp)
        temp = [int(char) for char in operation_index["constVal"]]
        result.extend(temp)
    # operation type
    else:
        
        temp = [int(char) for char in type_index["operation"]]
        result.extend(temp)
        # print(node.Type)
        
        if (node.Type == "and"):
            temp = [int(char) for char in operation_index["and"]]
            result.extend(temp)
        
        elif (node.Type == "or"):
            temp = [int(char) for char in operation_index["or"]]
            result.extend(temp)
        
        elif (node.Type == "Land"):
            temp = [int(char) for char in operation_index["and"]]
            result.extend(temp)
        
        elif (node.Type == "Lor"):
            temp = [int(char) for char in operation_index["or"]]
            result.extend(temp)
        
        elif (node.Type == "Uor"):
            temp = [int(char) for char in operation_index["or"]]
            result.extend(temp)
        
        elif (node.Type == "Uand"):
            temp = [int(char) for char in operation_index["and"]]
            result.extend(temp)
        
        elif (node.Type == "Unot"):
            temp = [int(char) for char in operation_index["not"]]
            result.extend(temp)
            
        elif (node.Type == "Ulnot"):
            temp = [int(char) for char in operation_index["not"]]
            result.extend(temp)
        else:
            pass

    return result

############################


input_nodes_list = []
node_sizes = {}


def get_nodes_sizes(nodes, input_output_wire):

    # getting inputs and their sizes
    for node, _ in nodes.items():
        if (node.Type == "INPUT"):
            input_nodes_list.append(node)
            node_sizes[node] = input_output_wire[0][node.name]
        elif (node.Type == "CONST"):
            input_nodes_list.append(node)
            node_sizes[node] = len(node.output)

    for input_node in input_nodes_list:
        DFS(input_node)

    # print(input_nodes_list)
    # print(node_sizes)

    for node, _ in nodes.items():
        if (node.Type == "CONCAT"):
            total_size = 0
            for connection in node.connections:
                if (connection.destination == node):
                    total_size += node_sizes[connection.source]
            node_sizes[node] = total_size
    return node_sizes


def DFS(current_node):
    # terminating condition
    # we reached an output node
    if (current_node.Type == "OUTPUT"):
        node_sizes[current_node] = current_node.size
        return
    # we reached a node with no connections
    elif (len(current_node.connections) == 0):
        return
    #################################################
    # recursive loop
    # get size of current node
    current_node_size = node_sizes[current_node]
    # get connections
    current_node_connections = current_node.connections
    for connection in current_node_connections:
        destination_node_size = 0
        destination_node = connection.destination
        already_calculated = (destination_node not in node_sizes)

        if (destination_node.Type == "REG" or destination_node.Type == "wire"):
            destination_node_size = destination_node.size
            node_sizes[destination_node] = destination_node_size
        elif (destination_node in node_sizes):
            # node size already calculated
            destination_node_size = node_sizes[destination_node]
            node_sizes[destination_node] = destination_node_size
        elif (connection.source_range is not None):
            # connection has source range
            destination_node_size = abs(
                connection.source_range[0]-connection.source_range[1])+1
            if (destination_node in node_sizes):
                node_sizes[destination_node] = max(
                    node_sizes[destination_node], destination_node_size)
            else:
                node_sizes[destination_node] = destination_node_size
        elif (connection.destination_range is not None):
            # connection has destination range
            destination_node_size = abs(
                connection.destination_range[0]-connection.destination_range[1])+1
            if (destination_node in node_sizes):
                node_sizes[destination_node] = max(
                    node_sizes[destination_node], destination_node_size)
            else:
                node_sizes[destination_node] = destination_node_size
        else:
            # connection uses the whole range
            destination_node_size = current_node_size
            if (destination_node in node_sizes):
                node_sizes[destination_node] = max(
                    node_sizes[destination_node], destination_node_size)
            else:
                node_sizes[destination_node] = destination_node_size

        # do the recursive call
        if (already_calculated):
            DFS(destination_node)
