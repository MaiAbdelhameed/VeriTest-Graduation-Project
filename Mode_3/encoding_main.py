# from Coverage.coverage import COVERAGE_MAIN
from PARSER.Simulate import PRASER_MAIN
from PARSER.GraphAPI import GraphAPI
from PARSER.code_to_graph import code_to_graph
from encoding_utils import get_encoding, get_nodes_sizes
from PARSER.components.Gates.bitwise import bitwise
import networkx as nx
import matplotlib.pyplot as plt
import os
import json
import sys


if len(sys.argv) < 2:
    print("Usage: python main.py <argument>")
    sys.exit(1)

filename = sys.argv[1]
# filename = "my_module.v"


G, input_output_wire = code_to_graph(filename)
print(input_output_wire)

pos = nx.spring_layout(G)  # Layout algorithm
# nx.draw(G, pos, with_labels=True, node_size=200, font_size=10, font_color="black")

# Draw edge labels
# edge_labels = {(u, v): f"{G[u][v]['edge_attr'][0].__str__()}" for u, v in G.edges}


# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# plt.show()


nodes = G.nodes()._nodes
edges = G.edges()._adjdict

# Nodes encoded matrix

nodes_encoded_matrix = []
edges_encoded_matrix = []
nodes_list = []

# calculate nodes size
nodes_sizes = get_nodes_sizes(nodes=nodes, input_output_wire=input_output_wire)

# nodes matrix
for node, _ in nodes.items():
    entry_list = []
    # type of the node
    entry_list.extend(get_encoding(node))
    ################################
    # number of connections
    number_of_connections = len(node.connections)
    if number_of_connections == 0:
        continue
    # entry_list.append(number_of_connections)
    ################################
    # size of node
    # entry_list.append(nodes_sizes[node])
    ################################
    nodes_encoded_matrix.append(entry_list)
    nodes_list.append(node)

# edges matrix

source_matrix = []
destination_matrix = []
edge_attribute_matrix = []
for source, destinations in edges.items():
    if destinations:
        for i in range(0, len(destinations)):
            source_matrix.append(nodes_list.index(source))
            destination_matrix.append(
                nodes_list.index(list(destinations.keys())[i]))
            # edge_attribute_matrix.append(
            # min(nodes_sizes[source], nodes_sizes[list(destinations.keys())[i]]))


for ind, n in enumerate(nodes_encoded_matrix):
    if n[0] == 1:
        for ind2, d in enumerate(destination_matrix):
            if ind == d:
                s = source_matrix[ind2]
                source_matrix[ind2] = ind
                destination_matrix[ind2] = s

    if n[1] == 1:
        for ind2, s in enumerate(source_matrix):
            if ind == s:
                d = destination_matrix[ind2]
                destination_matrix[ind2] = ind
                source_matrix[ind2] = d


edges_encoded_matrix.append(source_matrix)
edges_encoded_matrix.append(destination_matrix)
# print(nodes_encoded_matrix)
# print(edges_encoded_matrix)


# directory = "./"
directory = "final_model_utils"
filename = "test_sample_synth.txt"
file_path = os.path.join(directory, filename)


# lines = [nodes_encoded_matrix, edges_encoded_matrix, edge_attribute_matrix]
lines = [nodes_encoded_matrix, edges_encoded_matrix]

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Write lines to the file
with open(file_path, 'w') as file:
    json.dump(lines, file)
