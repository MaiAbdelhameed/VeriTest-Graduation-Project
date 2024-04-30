from Coverage.coverage import COVERAGE_MAIN
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
    "input": "10000",
    "output": "01000",
    "reg": "00100",
    "wire": "00010",
    "operation": "00001"
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
    "no_operation": "00000000000000000",
    "add": 			"00000000000000001",
    "and":			"00000000000000010",
    "or":			"00000000000000100",
    "xor":			"00000000000001000",
    "xnor":			"00000000000010000",
    "nor":			"00000000000100000",
    "nand":			"00000000001000000",
    "not":			"00000000010000000",
    "case":			"00000000100000000",
    "concat":		"00000001000000000",
    "conditional":	"00000010000000000",
    "constVal":		"00000100000000000",
    "mult":			"00001000000000000",
    "mux":			"00010000000000000",
    "power":		"00100000000000000",
    "shift":		"01000000000000000",
    "subtr":		"10000000000000000"
}


def get_encoding(node):
    result = []
    # input type
    if (isinstance(node, INPUT)):
        result.append(type_index["input"])
        result.append(operation_index["no_operation"])
    # output type
    elif (isinstance(node, OUTPUT)):
        result.append(type_index["output"])
        result.append(operation_index["no_operation"])
    # reg type
    elif (isinstance(node, REG)):
        result.append(type_index["reg"])
        result.append(operation_index["no_operation"])
    # wire type
    elif (isinstance(node, wire)):
        result.append(type_index["wire"])
        result.append(operation_index["no_operation"])
    # const value type
    elif (isinstance(node, ConstValue)):
        result.append(type_index["operation"])
        result.append(operation_index["constVal"])
    # operation type
    else:
        result.append(type_index["operation"])
        if (node.Type == "Adder"):
            result.append(operation_index["add"])
        elif (node.Type == "and"):
            result.append(operation_index["and"])
        elif (node.Type == "or"):
            result.append(operation_index["or"])
        elif (node.Type == "xor"):
            result.append(operation_index["xor"])
        elif (node.Type == "xnor"):
            result.append(operation_index["xnor"])
        elif (node.Type == "nor"):
            result.append(operation_index["nor"])
        elif (node.Type == "nand"):
            result.append(operation_index["nand"])
        elif (node.Type == "Case"):
            result.append(operation_index["case"])
        elif (node.Type == "CONCAT"):
            result.append(operation_index["concat"])
        elif (node.Type == "CONDITION"):
            result.append(operation_index["conditional"])
        elif (node.Type == "Land"):
            result.append(operation_index["and"])
        elif (node.Type == "Lor"):
            result.append(operation_index["or"])
        elif (node.Type == "Multplyer"):
            result.append(operation_index["mult"])
        elif (node.Type == "MUX"):
            result.append(operation_index["mux"])
        elif (node.Type == "power"):
            result.append(operation_index["power"])
        elif (node.Type == "shl"):
            result.append(operation_index["shift"])
        elif (node.Type == "shr"):
            result.append(operation_index["shift"])
        elif (node.Type == "subtractor"):
            result.append(operation_index["subtr"])
        elif (node.Type == "Uor"):
            result.append(operation_index["or"])
        elif (node.Type == "Uand"):
            result.append(operation_index["and"])
        elif (node.Type == "Unand"):
            result.append(operation_index["nand"])
        elif (node.Type == "Unor"):
            result.append(operation_index["nor"])
        elif (node.Type == "Uxor"):
            result.append(operation_index["xor"])
        elif (node.Type == "Uxnor"):
            result.append(operation_index["xnor"])
        elif (node.Type == "Unot"):
            result.append(operation_index["not"])
        elif (node.Type == "Ulnot"):
            result.append(operation_index["not"])
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
