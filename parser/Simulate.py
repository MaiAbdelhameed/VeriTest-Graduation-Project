from graph import parse_verilog_code
import networkx as nx
import matplotlib.pyplot as plt
from components.INPUT import INPUT

from components.ConstValue import ConstValue
from components.output import OUTPUT
from components.MUX import mux
from connection import connection



G, set_of_inputs, set_of_outputs = parse_verilog_code()
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=300, font_size=10, font_color="black", font_weight="bold")

# Draw edge labels
edge_labels = {(u, v): f"{G[u][v]['edge_attr'].__str__()}" for u, v in G.edges}


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()






# def finished(set_of_outputs):
#     for node in set_of_outputs:
#         calculated = node.calculate_output()
#         if calculated == False:
#             return False
#     return True



# def isInput(node, nodeadj):
#     if isinstance(node, mux):
#         for gate in node.G:
#             if gate == nodeadj:
#                 return True
#         if nodeadj == node.selector:
#             return True

#     for gate in node.G:
#         if gate == nodeadj:
#             return True
        
#     return False
    

def create_connection(gate, connection, G):
    connection.destination = gate
    G.add_edge(connection.source, gate, edge_attr=connection)


def search_for_connection(node, nodeadj):
    for connection in node.connections:
        if nodeadj == connection.destination:
            return connection


def DFS(node):
    for nodeadj in list(G.neighbors(node)):
        connection = search_for_connection(node, nodeadj)
        if node.process_node(connection):
            DFS(nodeadj)
        

DFS_START = list()
for IN in set_of_inputs:
    user_input = input(f"Enter {IN.name} ")
    const_node = ConstValue(user_input)
    G.add_node(const_node)
    connecting_edge = connection()
    connecting_edge.source = const_node
    connecting_edge.destination = IN
    const_node.add_connection(connecting_edge)
    IN.add_connection(connecting_edge)
    DFS_START.append(const_node)
    G.add_edge(const_node, IN, edge_attr = connecting_edge )
    

    



for node in DFS_START:
    DFS(node)





for node in G:
    if isinstance(node, OUTPUT):
        print(f"{node.name}: ","".join(node.output[::-1]))

    
    