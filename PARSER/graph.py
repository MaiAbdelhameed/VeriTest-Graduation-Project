
import networkx as nx
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
from PARSER.components.Gates.Ugate import UGate
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.REG import REG
from PARSER.components.Gates.MUX import mux
from PARSER.components.Gates.ConstValue import ConstValue
from PARSER.preprocessing.find import *
from PARSER.components.Gates.condgate import condgate
from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import *
from PARSER.connection import connection
from PARSER.components.Gates.bitwise import bitwise
from PARSER.components.Gates.concatenation import concatenation
from PARSER.components.Gates.Lconcatenation import Lconcatenation
from PARSER.components.Gates.Case import Case
from PARSER.components.Gates.adder import adder
from PARSER.components.Gates.subtractor import subtractor
from PARSER.components.Gates.multplyer import multplyer
from PARSER.components.Gates.shift import shift
from PARSER.components.Gates.power import power
from PARSER.components.Gates.Lgate import Lgate
from PARSER.components.Gates.Division import Division
from PARSER.components.Gates.Modulo import Modulo
import re
import os



def search_for_connection(node, nodeadj):
    list_of_connections = list()
    for connection in node.connections:
        if nodeadj == connection.destination and node == connection.source:
            list_of_connections.append(connection)

    
    return list_of_connections




def nodeingraph(G,a):
    for Nodeitr in G.nodes():
        if isinstance(Nodeitr, INPUT) or isinstance(Nodeitr, OUTPUT) or isinstance(Nodeitr, wire) or isinstance(Nodeitr, REG):
            if Nodeitr.name == a.name: return Nodeitr
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


def get_Instances(node):
    Instances = []

    if isinstance(node, Instance):
        # Add the assignment to the list
        Instances.append(node)

    # Recursively visit child nodes
    for child in node.children():
        Instances.extend(get_Instances(child))

    return Instances


def parse_verilog(file_path):
    # Parse the Verilog code
    ast, _ = parse([file_path])
    #ast.show()
    
    # Get all assignment statements from the AST
    assignments = get_assignments(ast)
    always_blocks = get_always_block(ast)
    Instances = get_Instances(ast)

    return assignments, always_blocks, Instances

def isGate(right):
    return isinstance(right, And) or isinstance(right, Or) or isinstance(right, Xor)

def isLGate(right):
    return isinstance(right, Land) or isinstance(right, Lor)


def Lgatetype(right):
    if isinstance(right, Land):
        return "Land"
    elif isinstance(right, Lor):
        return "Lor"


def isUGate(right):
    return isinstance(right, Uand) or isinstance(right, Uor) or isinstance(right, Uxor) or isinstance(right, Unot) or isinstance(right, Unand) or isinstance(right, Uxor) or isinstance(right, Xnor) or isinstance(right, Ulnot)
   

def gatetype(right):
    if isinstance(right, And):
        return "and"
    elif isinstance(right, Or):
        return "or"
    elif isinstance(right, Xor):
        return "xor"
    elif isinstance(right, Xnor):
        return "xnor"
    
    
   
def Ugatetype(right):
    if isinstance(right, Uand):
        return "Uand"
    elif isinstance(right, Uor):
        return "Uor"
    elif isinstance(right, Uxor):
        return "Uxor"
    elif isinstance(right, Unot):
        return "Unot"
    elif isinstance(right, Unand):
        return "Unand"
    elif isinstance(right, Uxnor):
        return "Uxnor"
    elif isinstance(right, Ulnot):
        return "Ulnot"
    

        
def connect_with_Dontcares(list_of_false_statments, G, list_of_upper_statements):
    list_of_statements = list()
    bind = None
    False_val_connection = None
    for statement in list_of_false_statments:
        if type(statement) == tuple:
            bind = statement[0]
            False_val_connection = statement[1]
        else:
            bind = statement.source.bind
            statement.source.bind = None ## remove the bind
            False_val_connection = statement

        mux2x1 = mux()
        if False_val_connection.destination == None:
            create_connection(mux2x1, False_val_connection, G, isFalseValue=True)
        else:
            create_connection(mux2x1, create_half_connection(False_val_connection.source), G, isFalseValue=True)

        mux2x1.set_bind(bind)
        connect_upper_common_connections_to_false_or_true_value(mux2x1, list_of_upper_statements, G, True) 
        list_of_statements.append(create_half_connection(mux2x1))
        

    return list_of_statements

def ports_intersect(connection1, connection2):
    if connection1.destination.name != connection2.destination.name:
        return None

    try:
        start1,end1 = connection1.destination_range
    except:
        start1 = 0
        end1 = connection1.destination.size - 1
    try:
        start2,end2 = connection2.destination_range
    except:
        start2 = 0
        end2 = connection2.destination.size - 1
    # 1 4
    # 3 8

    if start1 > end2 or start2 > end1:
        return None

    else:
        if start1 >= start2 and end1 <= end2:
            return [i for i in range(start1, end1 + 1)]
        elif start2 >= start1 and end2 <= end1:
            return [i for i in range(start2, end2 + 1)]
        elif start1 <= end2 and end1 >= end2:
            return [i for i in range(start1, end2 + 1)]
        elif start2 <= end1 and end2 >= end1:
            return [i for i in range(start2, end1 + 1)]
        else:
            return None


   
def connections_to_one_connection(connections):
    min_index = 9999
    max_index = -100
    for conn in connections:
        if conn.destination_range[0] < min_index:
            min_index = conn.destination_range[0]
            continue
        if conn.destination_range[0] > max_index:
            max_index = conn.destination_range[0]
            continue
        
    new_connection = connection()  
    new_connection.destination_range = (min_index, max_index)  
    new_connection.destination = connections[0].destination

    return new_connection
    

def merge_consecutive_connections(connections):
    ##try catch because merging mux bind has no source
    if len(connections) == 0:
        return
    try:
        mux_connections = connections[0].source.connections
    except:
        mux_connections = connections[0].destination.connections
    list_of_groups = list()
    list_of_groups.append([connections[0]])
    try:
        mux_connections.remove(connections[0])
    except:
        for conn in mux_connections:
            if conn.destination_range == connections[0].destination_range:
                mux_connections.remove(conn)
                break
        
        
    connections.remove(connections[0])
    

    fin_connections = list()
    for conn in connections:
        try:
            mux_connections.remove(conn)
        except:
            for conn2 in mux_connections:
                if conn2.destination_range == conn.destination_range:
                    mux_connections.remove(conn2)
                    break
        destVal = conn.destination_range[0]
        flag = True
        for group in list_of_groups:
            for conn2 in group:
                if abs(conn2.destination_range[0] - destVal) == 1:
                    group.append(conn) 
                    flag = False
                    break
        if flag:
            flag = True
            list_of_groups.append([conn])
    
    for group in list_of_groups:
        if len(group) > 1: 
            new_connection = connection()
            new_connection.source = group[0].source
            new_connection.destination = group[0].destination
            min_index = 9999
            max_index = -100
            for conn in group:
                if conn.destination_range[0] < min_index:
                    min_index = conn.destination_range[0]
                    continue
                if conn.destination_range[0] > max_index:
                    max_index = conn.destination_range[0]
                    continue
            new_connection.destination_range = (min_index, max_index)
            new_connection.source_range = (min_index, max_index)
            group.append(new_connection)

    
    for group in list_of_groups:
        fin_connections.append(group[-1])
        try:
            mux_connections.append(group[-1])
        except:
            pass

    while (len(connections) > 0):
        connections.pop()

    connections.extend(fin_connections)

def connect_upper_common_connections_to_false_or_true_value(mux2x1, list_of_upper_statements, G, value):
    for subst in list_of_upper_statements:
        if mux2x1.bind.destination == subst[0].destination and mux2x1.bind.destination_range ==subst[0].destination_range:
            if value:
                create_connection(mux2x1, subst[1], G, isTrueValue=True)
            else:
                create_connection(mux2x1, subst[1], G, isFalseValue=True)

            list_of_upper_statements.remove(subst)
            subst[0].destination.connections.remove(subst[0])


def connect_upper_common_connections_to_case(case, list_of_upper_statements, G):
    poss_cases = list()
    for conn in case.connections:
        if conn.port_number != None and conn.destination == case:
            poss_cases.append(conn.port_number)
    for subst in list_of_upper_statements.copy():
        if type(subst) == tuple:
            if case.bind.destination == subst[0].destination and case.bind.destination_range ==subst[0].destination_range:
                for vec in case.list_of_possible_cases:
                    if vec not in poss_cases:
                        subst[1].port_number = vec
                        
                        if subst[1].destination == None:
                            create_connection(case, subst[1], G)
                        else:
                            create_connection(case, create_half_connection(subst[1].source, port_number=vec), G)
                        
                list_of_upper_statements.remove(subst)
                subst[0].destination.connections.remove(subst[0])
                break
            else:
                intersection = ports_intersect(subst[0], case.bind)
                if intersection:
                    if subst[0].destination_range == None:
                        subst[0].destination.connections.remove(subst[0])
                        for index in range(subst[0].destination.size):
                            if index not in intersection:
                                conn = connection()
                                conn2 = connection()
                                conn.destination = subst[0].destination
                                conn2.source = subst[1].source
                                conn2.source_range = (index,index)
                                conn.destination_range = (index, index)
                                subst[0].destination.add_connection(conn)
                                new_subst = ()
                                new_subst = (conn, conn2)
                                list_of_upper_statements.append(new_subst)

                        list_of_upper_statements.remove(subst)
                            
                    
                    for bit in intersection:
                        conn = connection()
                        conn.source = subst[1].source
                        conn.source_range = (bit, bit)
                        for vec in case.list_of_possible_cases:
                            if vec not in poss_cases:
                                if conn.destination == None:
                                    conn.port_number = vec
                                    create_connection(case, conn, G)
                                else:
                                    create_connection(case, create_half_connection(conn.source, port_number=vec), G)

                        
        else: ## lazm arg3 recursivly s3b awyyyy!
            pass

def upper_common_connections(out_port, list_of_upper_statements, G):
    
    for subst in list_of_upper_statements:
        if type(subst) == tuple:
            if out_port.destination == subst[0].destination and out_port.destination_range == subst[0].destination_range and out_port.destination.name == subst[0].destination.name:
                subst[0].destination.connections.remove(subst[0])
                list_of_upper_statements.remove(subst)
                if isinstance(subst[1].source, ConstValue):
                    G.remove_node(subst[1].source)

            else:
                intersection = ports_intersect(subst[0], out_port)
                if intersection:
                    if subst[0].destination_range == None:
                        subst[0].destination.connections.remove(subst[0])
                        for index in range(subst[0].destination.size):
                            if index not in intersection:
                                conn = connection()
                                conn2 = connection()
                                conn.destination = subst[0].destination
                                conn2.source = subst[1].source
                                conn2.source_range = (index,index)
                                conn.destination_range = (index, index)
                                subst[0].destination.add_connection(conn)
                                subst[1].source.add_connection(conn2)
                                new_subst = ()
                                new_subst = (conn, conn2)
                                list_of_upper_statements.append(new_subst)

                        list_of_upper_statements.remove(subst)
                        
                        
                    
                    
                
        else: ## lazm arg3 recursivly w asheel kol el nodes s3ba awy!!!
            pass
           

        


def connect_with_Falsevalue(TargetConnection, list_of_false_statments, G, list_of_upper_statements):
    mux2x1 = mux()
    list_of_muxes = list()
    if isinstance(TargetConnection, tuple):
        create_connection(mux2x1, TargetConnection[1], G, isTrueValue=True)
        mux2x1.set_bind(TargetConnection[0])
        for false_statement in list_of_false_statments:
            if type(false_statement) == tuple: ## another non blocking sub or blocking
                if false_statement[0].destination == TargetConnection[0].destination and false_statement[0].destination_range == TargetConnection[0].destination_range:
                    create_connection(mux2x1, false_statement[1], G, isFalseValue=True)
                    TargetConnection[0].destination.connections.remove(false_statement[0]) ## remove this connection after merge
                    list_of_false_statments.remove(false_statement)
                    mux2x1.set_bind(TargetConnection[0])
                    upper_common_connections(false_statement[0], list_of_upper_statements, G)
                    
            
            else:
                if false_statement.source.bind.destination == TargetConnection[0].destination and false_statement.source.bind.destination_range == TargetConnection[0].destination_range:
                    create_connection(mux2x1, false_statement, G, isFalseValue=True)    
                    list_of_false_statments.remove(false_statement)
                    mux2x1.set_bind(false_statement.source.bind)
                    false_statement.bind = None
                    TargetConnection[0].destination.connections.remove(TargetConnection[0])
                    upper_common_connections(TargetConnection[0], list_of_upper_statements, G)
                    
                        
                    

                        
                
            
    else:
        create_connection(mux2x1, TargetConnection, G, isTrueValue=True)
        mux2x1.set_bind(TargetConnection.source.bind) 
        for false_statement in list_of_false_statments:
            if type(false_statement) == tuple:
                if TargetConnection.source.bind.destination == false_statement[0].destination and TargetConnection.source.bind.destination_range == false_statement[0].destination_range:
                    create_connection(mux2x1, false_statement[1], G, isFalseValue=True)
                    list_of_false_statments.remove(false_statement)
                    false_statement[0].destination.connections.remove(false_statement[0])
                    upper_common_connections(false_statement[0], list_of_upper_statements, G)
                   
                    
            else:
                if TargetConnection.source.bind.destination == false_statement.source.bind.destination and TargetConnection.source.bind.destination == false_statement.source.bind.destination_range:
                    create_connection(mux2x1, false_statement, G, isFalseValue=True)
                    list_of_false_statments.remove(false_statement)
                    
               

   


    
    

    if len(mux2x1.connections) == 1: ## No false value
        connect_upper_common_connections_to_false_or_true_value(mux2x1, list_of_upper_statements, G, False)
        

    list_of_muxes.append(create_half_connection(mux2x1))
    return list_of_muxes
    

def connect_default_value_to_case(connections, case, port_number, G):
    list_of_new_connections = list()
    for conn in connections:
        if type(conn) == tuple:
                if case.bind.destination == conn[0].destination and case.bind.destination_range == conn[0].destination_range:
                    conn[0].destination.connections.remove(conn[0])
                    conn[1].port_number = port_number
                    connections.remove(conn)
                    create_connection(case, conn[1], G)
                    break
                else:
                    intersection = ports_intersect(conn[0], case.bind)
                    
                    if intersection:
                        if conn[0].destination_range == None:
                            conn[0].destination.connections.remove(conn[0])
                            for index in range(conn[0].destination.size):
                                if index not in intersection:
                                    conn1 = connection()
                                    conn2 = connection()
                                    conn1.destination = conn[0].destination
                                    conn2.source = conn[1].source
                                    conn2.source_range = (index,index)
                                    conn1.destination_range = (index, index)
                                    conn[0].destination.add_connection(conn1)
                                    list_of_new_connections.append((conn1, conn2))
                                    
                                   
                            
                        
                        for bit in intersection:
                            conn1 = connection()
                            conn1.source = conn[1].source
                            conn1.source_range = (bit, bit)
                            conn1.port_number = "DEFAULT"
                            create_connection(case, conn1, G)
                        break

    return list_of_new_connections
def connect_with_another_case_statement(connections, list_of_case_gates, port_number, G, list_of_possible_cases):
    list_of_unconnected_connections = list()
    list_of_new_case_gates = list()
    list_of_connections = connections
    for conn in list_of_connections:
        isConnected = False
        for case_connection in list_of_case_gates:
            if type(conn) == tuple:
                if case_connection.source.bind.destination == conn[0].destination and case_connection.source.bind.destination_range == conn[0].destination_range:
                    conn[0].destination.connections.remove(conn[0])
                    conn[1].port_number = port_number
                    create_connection(case_connection.source, conn[1], G)
                    isConnected = True
                    break
                        
            else: ## mux
                if case_connection.source.bind.destination == conn.source.bind and case_connection.source.bind.destination_range == conn[0].destination_range:
                    conn.source.bind = None
                    conn.port_number = port_number
                    create_connection(case_connection.source, conn, G)
                    isConnected = True
                    break
        if not isConnected:
            list_of_unconnected_connections.append(conn)

    
    for conn in list_of_unconnected_connections:
        if type(conn) == tuple:
            case_gate = Case()
            case_gate.set_bind(conn[0])
            list_of_new_case_gates.append(create_half_connection(case_gate))
            conn[1].port_number = port_number
            if port_number == "DEFAULT":
                case_gate.list_of_possible_cases = list_of_possible_cases
            create_connection(case_gate, conn[1], G)
        
        else:
            case_gate = Case()
            if port_number == "DEFAULT":
                case_gate.list_of_possible_cases = list_of_possible_cases
            case_gate.set_bind(conn.source.bind)
            list_of_new_case_gates.append(create_half_connection(case_gate))
            conn.port_number = port_number
            create_connection(case_gate, conn, G)
            
    return list_of_new_case_gates

def parse_always_block(always, input_output_wire, G, list_of_upper_statements, start = 0, end = 1):
    if (always == None):
        
        return always
    
    if isinstance(always, ForStatement):
        pass
    

    if isGate(always):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Type = gatetype(always)
        Gate = bitwise(Type=Type)
        create_connection(Gate, right_connection, G)
        create_connection(Gate, left_connection, G)
        return create_half_connection(Gate)
    
    if isLGate(always):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Type = Lgatetype(always)
        L_gate = Lgate(Type=Type)
        create_connection(L_gate, right_connection, G)
        create_connection(L_gate, left_connection, G)
        return create_half_connection(L_gate)
    
    if isUGate(always):
        Type = Ugatetype(always)
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        if right_connection.source == None:
            right_connection.source = right_connection.destination
            right_connection.destination = None
        Single_input_Gate = UGate(Type = Type)
        create_connection(Single_input_Gate, right_connection, G)
        return create_half_connection(Single_input_Gate)

    if isinstance(always, Block):
        list_of_statements = list() 
        list_of_subst = list()
        for i in range(start, end,1):
            for statement in always.statements: ## rag3 b3d el for loop
                
                x = parse_always_block(statement, input_output_wire, G, list_of_statements)
                if type(x) == tuple:
                    list_of_statements.append(x)
                
                else:
                    list_of_statements.extend(x)
        
        
        return list_of_statements
            
    elif isinstance(always, IfStatement):

        list_of_true_statements = list()
        list_of_false_statments = list()
        true_statements = list()
        false_statements = list()
        if isinstance(always.true_statement,BlockingSubstitution) or isinstance(always.true_statement, NonblockingSubstitution):  
            true_statements = parse_always_block(always.true_statement, input_output_wire, G, list())
        else:
            true_statements = parse_always_block(always.true_statement, input_output_wire, G, list_of_upper_statements)

        if isinstance(always.false_statement,BlockingSubstitution) or isinstance(always.false_statement, NonblockingSubstitution):  
            false_statements = parse_always_block(always.false_statement, input_output_wire, G, list())
        else:
            false_statements = parse_always_block(always.false_statement, input_output_wire, G, list_of_upper_statements)
        
        if type(true_statements) == tuple:
            list_of_true_statements.append(true_statements)
        elif type(true_statements) == list:
            list_of_true_statements.extend(true_statements)
        else:
            pass

        if type(false_statements) == tuple:
            list_of_false_statments.append(false_statements)
        elif type(false_statements) == list:
            list_of_false_statments.extend(false_statements)
        else:
            pass

        list_of_statements = list()
        for true_statement in list_of_true_statements:
            connecting_edges = connect_with_Falsevalue(true_statement, list_of_false_statments, G, list_of_upper_statements)
            for mux2x1 in connecting_edges:
                sel = parse_always_block(always.cond, input_output_wire, G, list_of_upper_statements)
                if sel.source == None:
                    sel.source = sel.destination
                    sel.destination = None
                create_connection(mux2x1.source, sel, G, isSelector=True)
                
            
            list_of_statements.extend(connecting_edges)


        

        connecting_edges = connect_with_Dontcares(list_of_false_statments, G, list_of_upper_statements)
        

        for mux2x1 in connecting_edges:
            sel = parse_always_block(always.cond, input_output_wire, G, list_of_upper_statements)
            if sel.source == None:
                sel.source = sel.destination
                sel.destination = None
            create_connection(mux2x1.source, sel, G, isSelector=True)
                
            
        list_of_statements.extend(connecting_edges)



        return list_of_statements

        
        
    if isinstance(always, Partselect):
        connecting_edge = parse_always_block(always.var, input_output_wire, G, list_of_upper_statements)
        msb = int(always.msb.value)
        lsb = int(always.lsb.value)
        if lsb > msb:
            temp = lsb
            lsb = msb
            msb = temp
        if connecting_edge.source == None:
            connecting_edge.destination_range = (lsb, msb)
        else:
            connecting_edge.source_range = (lsb, msb)

        return connecting_edge
    
    if isinstance(always, Concat) and not isinstance(always, LConcat): 
        concat_gate = concatenation()
        for index, element in enumerate(always.list):
            concat_element_connection = parse_always_block(element, input_output_wire, G, list_of_upper_statements)
            concat_element_connection.port_number = index
            create_connection(concat_gate, concat_element_connection, G)

        return create_half_connection(concat_gate)
    
    if isinstance(always, Cond):
        true_value_connection = parse_always_block(always.false_value, input_output_wire, G, list_of_upper_statements)
        false_value_connection = parse_always_block(always.true_value, input_output_wire, G, list_of_upper_statements)
        if true_value_connection.source == None:
            true_value_connection.source = true_value_connection.destination
            true_value_connection.destination = None
        if false_value_connection.source == None:
            false_value_connection.source = false_value_connection.destination
            false_value_connection.destination = None
        sel_connection = parse_always_block(always.cond, input_output_wire, G, list_of_upper_statements)

        if isinstance(sel_connection.source, INPUT): 
            condition_gate = condgate("eq")
            create_connection(condition_gate, sel_connection, G)
            sel_connection = create_half_connection(condition_gate)
        
        mux2x1 = mux()

        create_connection(mux2x1, true_value_connection, G, isTrueValue=True)
        create_connection(mux2x1, false_value_connection, G, isFalseValue=True)
        create_connection(mux2x1, sel_connection, G, isSelector=True)
        return create_half_connection(mux2x1)



    if isinstance(always, Srl) or isinstance(always, Sra):
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        shift_gate = shift("shr")
        create_connection(shift_gate, right_connection, G)
        create_connection(shift_gate, left_connection, G, isShiftVector=True)
        return create_half_connection(shift_gate)
    
    if isinstance(always, Divide):
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        Division_gate  = Division()
        create_connection(Division_gate, right_connection, G)
        create_connection(Division_gate, left_connection, G, isNumerator = True)
        return create_half_connection(Division_gate)
    
    if isinstance(always, Mod):
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        Modulo_gate  = Modulo()
        create_connection(Modulo_gate, right_connection, G)
        create_connection(Modulo_gate, left_connection, G, isNumerator = True)
        return create_half_connection(Modulo_gate)

    if isinstance(always, Sll) or isinstance(always, Sla):
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        shift_gate = shift("shl")
        create_connection(shift_gate, right_connection, G)
        create_connection(shift_gate, left_connection, G, isShiftVector=True)
        return create_half_connection(shift_gate)


        

    if isinstance(always, Pointer):
        connecting_edge = parse_always_block(always.var, input_output_wire, G, list_of_upper_statements)
        value = int(always.ptr.value)
        # connecting_edge.source_range = (value, value)
        if connecting_edge.source == None:
            connecting_edge.destination_range = (value, value)
        else:
            connecting_edge.source_range = (value, value)

        return connecting_edge
        

    
    if isinstance(always, IntConst): ## missing
        value = always.value
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
        Constant_node = ConstValue(CONST = fin_value)
        G.add_node(Constant_node)
        return create_half_connection(Constant_node)
    

    if isinstance(always, LessEq):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("le", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(always, GreaterEq):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("ge", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    if isinstance(always, NotEq):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("ne", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
        
    
    if isinstance(always, LessThan):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("lt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(always, GreaterThan):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("gt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    
    if isinstance(always, Eq):
        lhs_node_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        rhs_value_node_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        condition_gate_connecting_edge = create_condition("eq", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    if isinstance(always, ForStatement):
        input_output_wire[4][always.cond.left.name] = 0
        parse_always_block(always.statement, input_output_wire, G, list_of_upper_statements, start = 0, end= int(always.cond.right.value) )
        pass

    

    elif isinstance(always, NonblockingSubstitution) or isinstance(always, BlockingSubstitution):

        list_of_tups = list()
        left = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        right = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        if type(left) == list:
            L_concat_gate = Lconcatenation()
            create_connection(L_concat_gate, right, G)
            for conn in left:
                tup = (conn, create_half_connection(L_concat_gate, src_range=conn.source_range))
                list_of_tups.append(tup)
                upper_common_connections(conn, list_of_upper_statements, G)

            return list_of_tups

            
        upper_common_connections(left, list_of_upper_statements, G)     #edit lw left mwgood fel right
        tup = (left, right)
        return tup
    
    elif isinstance(always, Lvalue) or isinstance(always, Rvalue):
        return parse_always_block(always.var, input_output_wire, G, list_of_upper_statements)
    
    elif isinstance(always, LConcat):
        concat_gate = Lconcatenation()
        list_of_L_connections = list()
        start_range = 0
        for index, element in enumerate(always.list[::-1]):
            concat_element_connection = parse_always_block(element, input_output_wire, G, list_of_upper_statements)
            concat_element_connection.port_number = index
            if concat_element_connection.destination_range == None:
                concat_element_connection.source_range = (start_range, start_range+ concat_element_connection.destination.size - 1)
                start_range += concat_element_connection.destination.size
            else:
                start,end = concat_element_connection.destination_range
                size = abs(start-end) + 1
                concat_element_connection.source_range = (start_range, start_range+ size - 1)
                start_range += size

            list_of_L_connections.append(concat_element_connection)
        
        return list_of_L_connections

    

    elif isinstance(always, Power):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Power_gate = power()
        create_connection(Power_gate, right_connection, G)
        create_connection(Power_gate, left_connection, G, isPowered = True)
        return create_half_connection(Power_gate)

    elif isinstance(always, Plus):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Adder = adder()
        create_connection(Adder, right_connection, G)
        create_connection(Adder, left_connection, G)
        return create_half_connection(Adder)


    elif isinstance(always, Minus):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Subtractor = subtractor()
        create_connection(Subtractor, right_connection, G)
        create_connection(Subtractor, left_connection, G)
        return create_half_connection(Subtractor)

    
    elif isinstance(always, Times):
        right_connection = parse_always_block(always.right, input_output_wire, G, list_of_upper_statements)
        left_connection = parse_always_block(always.left, input_output_wire, G, list_of_upper_statements)
        Multplyer = multplyer()
        create_connection(Multplyer, right_connection, G)
        create_connection(Multplyer, left_connection, G)
        return create_half_connection(Multplyer)

    elif isinstance(always, CaseStatement):
        list_of_case_statements = list()
        list_of_all_possible_cases = list()
        for case in always.caselist:
            if case.cond == None:
                port_number = "DEFAULT"
            else:
                const_node_connection = parse_always_block(case.cond[0], input_output_wire, G, list())
                if isinstance(const_node_connection.source, ConstValue):
                    G.remove_node(const_node_connection.source)
                port_number = const_node_connection.source.output
                list_of_all_possible_cases.append(port_number)
            
            connections = list()
            if isinstance(case.statement, NonblockingSubstitution) or isinstance(case.statement, BlockingSubstitution):
                connections = parse_always_block(case.statement, input_output_wire, G, list())
            else:
                connections = parse_always_block(case.statement, input_output_wire, G, list_of_upper_statements)
            list_of_connections = list()
            if type(connections) == tuple:
                list_of_connections.append(connections)
            else:
                list_of_connections.extend(connections)

            list_of_new_case_gates = list()
            if port_number == "DEFAULT":
                for case in list_of_case_statements:
                    case.source.list_of_possible_cases = list_of_all_possible_cases
                    list_of_new_connections = connect_default_value_to_case(list_of_connections,case.source,port_number, G)
                    if list_of_new_connections:
                        list_of_connections = list_of_new_connections
            else:
                list_of_new_case_gates = connect_with_another_case_statement(list_of_connections, list_of_case_statements, port_number, G, list_of_all_possible_cases)

            list_of_case_statements.extend(list_of_new_case_gates)
            for case_connection in list_of_new_case_gates:
                compare_connection = parse_always_block(always.comp, input_output_wire, G, list())
                create_connection(case_connection.source, compare_connection, G, isSelector=True)
        

        for case_connection in list_of_case_statements:
            ##CHECK SIZE??!!
            connect_upper_common_connections_to_case(case_connection.source, list_of_upper_statements, G)
            
        
        return list_of_case_statements     
            
            

    
    
    else: 
        name_of_variable = always.name
        search_for_input = None
        Type = None
        connecting_edge = connection()

        ## SEARCH FOR INPUT OR OUTPUT OR WIRE ##
        if name_of_variable in input_output_wire[0]: 
            Type = "INPUT"
            size = input_output_wire[0][name_of_variable]
            search_for_input = INPUT(Type="INPUT", name=name_of_variable, top_level=0)

        elif name_of_variable in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", name=name_of_variable, size = size, top_level=0)
            
        elif name_of_variable in input_output_wire[2]:
            Type = "WIRE"
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", name=name_of_variable, size = size)
        
        elif name_of_variable in input_output_wire[3]:
            Type = "REG"
            size = input_output_wire[3][name_of_variable]
            search_for_input = REG(Type="REG", name=name_of_variable, size = size)


        node_itr = nodeingraph(G, search_for_input)
        if Type == "INPUT":
            return create_half_connection(node_itr)
        else:
            connecting_edge.destination = node_itr
            node_itr.add_connection(connecting_edge)
            return connecting_edge

def create_out_connection(assignment, input_output_wire, G):

    if isinstance(assignment, Partselect):
        connecting_edge = create_out_connection(assignment.var, input_output_wire, G)
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        if lsb > msb:
            temp = lsb
            lsb = msb
            msb = temp
        connecting_edge.destination_range = (lsb, msb)
        return connecting_edge
    elif isinstance(assignment, Pointer):
        connecting_edge = create_out_connection(assignment.var, input_output_wire, G)
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
            search_for_input = OUTPUT(Type="OUTPUT", name=name_of_variable, size = size, top_level=0)
            
        elif name_of_variable in input_output_wire[2]:
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", name=name_of_variable, size = size)

        elif name_of_variable in input_output_wire[3]:
            size = input_output_wire[3][name_of_variable]
            search_for_input = REG(Type="REG", name=name_of_variable, size = size)
        else: ## undefined wire
            if name_of_variable not in input_output_wire[3]:
                size = 1
                WIRE_NODE = wire(Type = "WIRE", name=name_of_variable, size = size, endian="little") 
                G.add_node(WIRE_NODE)
                input_output_wire[3][name_of_variable] = size

            search_for_input = wire(Type = "WIRE", name=name_of_variable, size = size)        

        node_itr = nodeingraph(G, search_for_input)
        if node_itr == None: 
            search_for_input.add_connection(connecting_edge)
            connecting_edge.destination = search_for_input
            return connecting_edge
                
        else:
            node_itr.add_connection(connecting_edge)
            connecting_edge.destination = node_itr
            return connecting_edge
    

## creating a connection and setting its source to be the passed Gate ##
def create_half_connection(Gate, dst_range = None, port_number = None, src_range = None):
    connecting_edge = connection()
    connecting_edge.destination_range = dst_range
    connecting_edge.port_number = port_number
    connecting_edge.source_range = src_range
    Gate.add_connection(connecting_edge)
    connecting_edge.source = Gate
    return connecting_edge


## connecting the destination of the passed connection to be the gate node ##
def create_connection(gate, connection, G, isTrueValue = False, isFalseValue = False, isSelector = False, isPowered = False, isShiftVector = False, isNumerator = False):
    if connection.source == None:
        connection.source = connection.destination
        connection.destination = None
        connection.source_range = connection.destination_range
        connection.destination_range = None
    connection.destination = gate
    connection.isTrueValue = isTrueValue
    connection.isFalseValue = isFalseValue
    connection.isSelector = isSelector
    connection.isPowered = isPowered
    connection.isShiftVector = isShiftVector
    connection.isNumerator = isNumerator
    gate.add_connection(connection)
    edge_attr = list()
    try:edge_attr = G.edges[connection.source, gate]["edge_attr"]
    except: pass
    edge_attr.append(connection)
    G.add_edge(connection.source, gate, edge_attr=edge_attr)

def convert_to_binary(fin_value, type_of_value):
    hex_map = {hex(i)[2:].upper(): f"{bin(i)[2:]:>04}" for i in range(16)}
    if type_of_value == "b":
        return fin_value
    elif type_of_value == "h":
        return "".join(hex_map.get(hex_digit) for hex_digit in fin_value)
    elif type_of_value == "d":
        return bin(int(fin_value))[2:]


## creating a condition gate and return its connection, this gate output either 1 or 0 ##
def create_condition(condition, lhs_value_node_connection, rhs_value_node_connection, G):
    condition_gate = condgate(condition)
    
    create_connection(condition_gate, lhs_value_node_connection, G)
    create_connection(condition_gate, rhs_value_node_connection, G)    
    return create_half_connection(condition_gate)

def parse_assign_statement(assignment, input_output_wire, G):

    if isGate(assignment):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Type = gatetype(assignment)
        Gate = bitwise(Type=Type)
        create_connection(Gate, right_connection, G)
        create_connection(Gate, left_connection, G)
        return create_half_connection(Gate)
    

    elif isinstance(assignment, Power):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Power_gate = power()
        create_connection(Power_gate, right_connection, G)
        create_connection(Power_gate, left_connection, G, isPowered = True)
        return create_half_connection(Power_gate)
    

    elif isinstance(assignment, Times):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Multplyer = multplyer()
        create_connection(Multplyer, right_connection, G)
        create_connection(Multplyer, left_connection, G)
        return create_half_connection(Multplyer)
    

    elif isinstance(assignment, Plus):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Adder = adder()
        create_connection(Adder, right_connection, G)
        create_connection(Adder, left_connection, G)
        return create_half_connection(Adder)
    
    elif isinstance(assignment, Minus):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Subtractor = subtractor()
        create_connection(Subtractor, right_connection, G)
        create_connection(Subtractor, left_connection, G)
        return create_half_connection(Subtractor)

    if isLGate(assignment):
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        Type = Lgatetype(assignment)
        L_gate = Lgate(Type=Type)
        create_connection(L_gate, right_connection, G)
        create_connection(L_gate, left_connection, G)
        return create_half_connection(L_gate)
    

    if isinstance(assignment, Srl) or isinstance(assignment, Sra):
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        shift_gate = shift("shr")
        create_connection(shift_gate, right_connection, G)
        create_connection(shift_gate, left_connection, G, isShiftVector=True)
        return create_half_connection(shift_gate)
    

    if isinstance(assignment, Sll) or isinstance(assignment, Sla): 
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        shift_gate = shift("shl")
        create_connection(shift_gate, right_connection, G)
        create_connection(shift_gate, left_connection, G, isShiftVector=True)
        return create_half_connection(shift_gate)
    
    
    
    if isinstance(assignment, Partselect):
        connecting_edge = parse_assign_statement(assignment.var, input_output_wire, G)
        msb = int(assignment.msb.value)
        lsb = int(assignment.lsb.value)
        if lsb > msb:
            temp = lsb
            lsb = msb
            msb = temp
        connecting_edge.source_range = (lsb, msb)
        return connecting_edge
    
    if isinstance(assignment, Concat): 
        concat_gate = concatenation()
        for index, element in enumerate(assignment.list):
            concat_element_connection = parse_assign_statement(element, input_output_wire, G)
            concat_element_connection.port_number = index
            create_connection(concat_gate, concat_element_connection, G)

        return create_half_connection(concat_gate)
    
    if isinstance(assignment, Cond):
        true_value_connection = parse_assign_statement(assignment.true_value, input_output_wire, G)
        false_value_connection = parse_assign_statement(assignment.false_value, input_output_wire, G)
        sel_connection = parse_assign_statement(assignment.cond, input_output_wire, G)

        ## in case that the sel_edge source was an Input, in this case
        ## we will first connect the input to a condition gate to compare it with 1's
        if isinstance(sel_connection.source, INPUT): 
            condition_gate = condgate("eq")
            create_connection(condition_gate, sel_connection, G)
            sel_connection = create_half_connection(condition_gate)
        
        mux2x1 = mux()
        create_connection(mux2x1, true_value_connection, G, isTrueValue=True)
        create_connection(mux2x1, false_value_connection, G, isFalseValue=True)
        create_connection(mux2x1, sel_connection, G, isSelector=True)
        return create_half_connection(mux2x1)

    if isinstance(assignment, Divide):
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        Division_gate  = Division()
        create_connection(Division_gate, right_connection, G)
        create_connection(Division_gate, left_connection, G, isNumerator = True)
        return create_half_connection(Division_gate)
    
    if isinstance(assignment, Mod):
        left_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        Division_gate  = Modulo()
        create_connection(Division_gate, right_connection, G)
        create_connection(Division_gate, left_connection, G, isNumerator = True)
        return create_half_connection(Division_gate)

    
    if isinstance(assignment, Pointer):
        connecting_edge = parse_assign_statement(assignment.var, input_output_wire, G)
        value = int(assignment.ptr.value)
        connecting_edge.source_range = (value, value)
        return connecting_edge

    
    if isinstance(assignment, IntConst): ## missing
        value = assignment.value
        fin_value = re.search(r"(?:\d+'\w)?(\d+|\w+)", value).group(1)
        type_of_value = re.findall("\d+'(\w)(?:\d+|\w+)", value)
        if len(type_of_value) == 0: type_of_value = "d"
        else: type_of_value = type_of_value[0]
            
        fin_value = convert_to_binary(fin_value, type_of_value)
        

        Constant_node = ConstValue(CONST = fin_value)
        G.add_node(Constant_node)
        return create_half_connection(Constant_node)
    

    if isinstance(assignment, LessEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("le", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(assignment, GreaterEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("ge", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    if isinstance(assignment, NotEq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("ne", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
        
    
    if isinstance(assignment, LessThan):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("lt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge

    if isinstance(assignment, GreaterThan):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("gt", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
    
    
    if isinstance(assignment, Eq):
        lhs_node_connection = parse_assign_statement(assignment.left, input_output_wire, G)
        rhs_value_node_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        condition_gate_connecting_edge = create_condition("eq", lhs_node_connection, rhs_value_node_connection, G)
        return condition_gate_connecting_edge
        
    

    if isUGate(assignment):
        Type = Ugatetype(assignment)
        right_connection = parse_assign_statement(assignment.right, input_output_wire, G)
        Single_input_Gate = UGate(Type = Type)
        create_connection(Single_input_Gate, right_connection, G)
        return create_half_connection(Single_input_Gate)
        
        


    else: 
        name_of_variable = assignment.name
        search_for_input = None
        Type = None
        connecting_edge = connection()

        ## SEARCH FOR INPUT OR OUTPUT OR WIRE ##
        if name_of_variable in input_output_wire[0]: 
            Type = "INPUT"
            size = input_output_wire[0][name_of_variable]
            search_for_input = INPUT(Type="INPUT", name=name_of_variable, top_level=0)

        elif name_of_variable in input_output_wire[1]:
            Type = "OUTPUT"
            size = input_output_wire[1][name_of_variable]
            search_for_input = OUTPUT(Type="OUTPUT", name=name_of_variable, size = size, top_level=0)
            
        elif name_of_variable in input_output_wire[2]:
            Type = "WIRE"
            size = input_output_wire[2][name_of_variable]
            search_for_input = wire(Type="WIRE", name=name_of_variable, size = size)

        elif name_of_variable in input_output_wire[3]:
            Type = "REG"
            size = input_output_wire[3][name_of_variable]
            search_for_input = REG(Type="REG", name=name_of_variable, size = size)
        


        node_itr = nodeingraph(G, search_for_input)
        return create_half_connection(node_itr)
            
    ## OUTPUT PORT IS CONNECTION1
def merge_connections(connection1, connection2):

    if connection1.destination == connection2.source:  ## there is double connection in same node
        connection1.destination.connections.remove(connection1)

   
    connection1.source = connection2.source
    connection1.source_range = connection2.source_range
    connection2.source.connections.remove(connection2)
    connection1.source.add_connection(connection1)

    return connection1

    

def get_file_name(module_name):

    files = os.listdir("PARSER/files")
    for filename in files:
        if filename.endswith(".v"):
            with open("PARSER/files/"+ filename, "r") as file:
                content = file.read()
              
                if re.findall(module_name, content, flags = re.MULTILINE):
                    return "PARSER/files/" + filename
                


def replace_node(graph, node_to_replace, new_node):
    for nodeadj in list(graph.neighbors(node_to_replace)):
        connections = graph.edges[node_to_replace, nodeadj]["edge_attr"]
        for connection in connections:
            connection.source = new_node
            new_node.add_connection(connection)
        graph.add_edge(new_node, nodeadj, edge_attr = connections)

def find_matched_connection(connections, connection):
    for conn in connections:
        if conn.destination_range == connection.destination_range:
            return conn


def replace_node_output(graph, node_to_replace, new_node):
    for connection in node_to_replace.connections:
        if connection.destination == node_to_replace:
            connection.destination = new_node
            edge_attr = list()
            try:edge_attr = graph.edges[connection.source, new_node]["edge_attr"]
            except: pass
            edge_attr.append(connection)
            graph.add_edge(connection.source, new_node, edge_attr = edge_attr)
            
        elif connection.source == node_to_replace:
            connection.source = new_node
            edge_attr = list()
            try:edge_attr = graph.edges[new_node, connection.destination]["edge_attr"]
            except: pass
            edge_attr.append(connection)
            graph.add_edge(new_node, connection.destination, edge_attr = edge_attr)

        new_node.add_connection(connection)




    
def parse_gate_level(port_list, G, Type, input_output_wire):
    stack_of_connections = list()
    array_of_connections = list()
    port_list = [i for i in port_list]

    output_connection = create_out_connection(port_list[0].argname, input_output_wire, G)
    first_arg = parse_assign_statement(port_list[1].argname, input_output_wire, G)
    stack_of_connections.append(first_arg)
    port_list.pop(0)
    port_list.pop(0)
    for port in port_list:
        array_of_connections.append(parse_assign_statement(port.argname, input_output_wire, G))

    

    if Type == "not":
        UNOT = UGate(Type = "Unot")
        create_connection(UNOT, stack_of_connections[-1], G)
        stack_of_connections.append(create_half_connection(UNOT))
        
    for conn in array_of_connections:    
        Gate = bitwise(Type=Type)
        create_connection(Gate, stack_of_connections[-1], G)
        create_connection(Gate, conn, G)
        stack_of_connections.append(create_half_connection(Gate))


    
    merged_connection = merge_connections(connection1=output_connection, connection2=stack_of_connections[-1])
    edge_attr = list()
    try:edge_attr = G.edges[merged_connection.source, merged_connection.destination]["edge_attr"]
    except: pass
    edge_attr.append(merged_connection)
    G.add_edge(merged_connection.source, merged_connection.destination, edge_attr = edge_attr)
def parse_verilog_code(module_path, top_level):
    
 
    assignments, always_blocks, instances = parse_verilog(module_path)

    G = nx.DiGraph()
    input_output_wire2, portlist = get_input_output(module_path)
    input_output_wire = input_output_wire2.copy()
    endians_dict = dict()
    for key, value in input_output_wire[0].items():
        input_output_wire[0][key] = abs(int(value["msb"]) - int(value["lsb"])) + 1
        if int(value["lsb"]) > int(value["msb"]):
            endians_dict.update({key: "big"})
        else:
            endians_dict.update({key: "little"})

    
    for key, value in input_output_wire[1].items():
        input_output_wire[1][key] = abs(int(value["msb"]) - int(value["lsb"])) + 1
        if int(value["lsb"]) > int(value["msb"]):
            endians_dict.update({key: "big"})
        else:
            endians_dict.update({key: "little"})


    for key, value in input_output_wire[2].items():
        input_output_wire[2][key] = abs(int(value["msb"]) - int(value["lsb"])) + 1
        if int(value["lsb"]) > int(value["msb"]):
            endians_dict.update({key: "big"})
        else:
            endians_dict.update({key: "little"})


    for key, value in input_output_wire[3].items():
        input_output_wire[3][key] = abs(int(value["msb"]) - int(value["lsb"])) + 1
        if int(value["lsb"]) > int(value["msb"]):
            endians_dict.update({key: "big"})
        else:
            endians_dict.update({key: "little"})


    
    
    for key,value in input_output_wire[1].items():
        endian = endians_dict[key]
        OUTPUT_NODE = OUTPUT(Type="OUTPUT", name = key, size = value, top_level = top_level, endian=endian)
        G.add_node(OUTPUT_NODE)
    
    for key,value in input_output_wire[0].items():
        endian = endians_dict[key]
        INPUT_NODE = INPUT(Type="INPUT", name = key, top_level = top_level, endian = endian)
        G.add_node(INPUT_NODE)

    for key,value in input_output_wire[3].items():
        endian = endians_dict[key]
        REG_NODE = REG(Type="REG", name = key, size = value, endian = endian)
        G.add_node(REG_NODE)


    for key,value in input_output_wire[2].items():
        endian = endians_dict[key]
        WIRE_NODE = wire(Type="WIRE", name = key, size = value, endian = endian)
        G.add_node(WIRE_NODE)



    input_output_wire.append(dict())
    for assignment in assignments:
        final_output_connection = parse_assign_statement(assignment.right.var, input_output_wire, G)
        output_port_connection = create_out_connection(assignment.left.var, input_output_wire, G)
        merged_connection = merge_connections(output_port_connection, final_output_connection)
        edge_attr = list()
        try:edge_attr = G.edges[merged_connection.source, merged_connection.destination]["edge_attr"]
        except: pass
        edge_attr.append(merged_connection)
        G.add_edge(merged_connection.source, merged_connection.destination, edge_attr = edge_attr)


    for instance in instances:
        if instance.module.lower() == "or" or instance.module.lower() == "and" or instance.module.lower() == "xor" or instance.module.lower() == "nand" or instance.module.lower() == "nor" or instance.module.lower() == "xnor" or instance.module.lower() == "not":
            parse_gate_level(instance.portlist, G, instance.module, input_output_wire)
        else:
            file_name = get_file_name(instance.module)
            graph, portlist = parse_verilog_code(file_name, top_level=False)
            G = nx.compose(G, graph)
            G2 = G.copy()
            for index, port in enumerate(instance.portlist):
                for node in graph.nodes():
                    if port.portname == None:
                        port.portname = portlist[index].name
                    if isinstance(node, INPUT) or isinstance(node, OUTPUT) or isinstance(node, Wire) or isinstance(node, REG):
                        if node.name == port.portname:
                            for n in G2:
                                if isinstance(n, INPUT):
                                    if port.argname.name == n.name:
                                        replace_node(G, node, n)
                                elif isinstance(n, OUTPUT):
                                        if port.argname.name == n.name:
                                            replace_node_output(G, node, n)
                        nx.set_node_attributes(G, {node: True}, name="removal")
                    else:
                        nx.set_node_attributes(G, {node: False}, name="removal")

            
            G3 = graph.copy()
            for node in G3:
                if G.nodes[node]["removal"] == True:
                    G.remove_node(node)

            
                                    
            
            
        
        
        

        
        


    


    for always in always_blocks:
        list_of_upper_statements = list()
        mux_connections = parse_always_block(always.statement, input_output_wire, G, list_of_upper_statements)
        for mux_connection in mux_connections:
            if type(mux_connection) == tuple:
                if mux_connection[1].source == None:
                    mux_connection[1].source = mux_connection[1].destination
                    mux_connection[1].destination = None
                merged_connection = merge_connections(mux_connection[0], mux_connection[1])
                edge_attr = list()
                try:edge_attr = G.edges[merged_connection.source, merged_connection.source.destination]["edge_attr"]
                except: pass
                edge_attr.append(merged_connection)
                G.add_edge(merged_connection.source, merged_connection.destination, edge_attr = edge_attr)
            elif isinstance(mux_connection, connection) : #mux
                merged_connection = merge_connections(mux_connection.source.bind, mux_connection)
                edge_attr = list()
                try:edge_attr = G.edges[merged_connection.source, merged_connection.destination]["edge_attr"]
                except: pass
                edge_attr.append(merged_connection)
                G.add_edge(merged_connection.source, merged_connection.destination, edge_attr = edge_attr)
                

        

    return G, portlist, input_output_wire







    





