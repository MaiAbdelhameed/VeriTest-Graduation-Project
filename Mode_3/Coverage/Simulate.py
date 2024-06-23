from graph import parse_verilog_code
import networkx as nx
import matplotlib.pyplot as plt
from components.ConstValue import ConstValue
from components.output import OUTPUT
from connection import connection
from components.INPUT import INPUT


G, set_of_inputs, set_of_outputs = parse_verilog_code()
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=300,
        font_size=10, font_color="black", font_weight="bold")

# Draw edge labels
edge_labels = {(u, v): f"{G[u][v]['edge_attr'].__str__()}" for u, v in G.edges}


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# plt.show()


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
    list_of_connections = list()
    for connection in node.connections:
        if nodeadj == connection.destination:
            list_of_connections.append(connection)

    return list_of_connections


def DFS(node):
    for nodeadj in list(G.neighbors(node)):
        connection = search_for_connection(node, nodeadj)
        if node.process_node(connection):
            DFS(nodeadj)


DFS_START = list()
G2 = G.copy()

for node in G2.nodes():
    if isinstance(node, INPUT):
        user_input = input(f"Enter {node.name} ")
        const_node = ConstValue(user_input)
        G.add_node(const_node)
        connecting_edge = connection()
        connecting_edge.source = const_node
        connecting_edge.destination = node
        const_node.add_connection(connecting_edge)
        node.add_connection(connecting_edge)
        DFS_START.append(const_node)
        G.add_edge(const_node, node, edge_attr=connecting_edge)
    elif isinstance(node, ConstValue):
        DFS_START.append(node)


for node in DFS_START:
    DFS(node)


for node in G:
    if isinstance(node, OUTPUT):
        print(f"{node.name}: ", "".join(node.output))
