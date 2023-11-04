import networkx as nx
from node import *
import matplotlib.pyplot as plt
from type_of_node import *


node1 = node(type_of_node.INPUT.name)
node2 = node(type_of_node.AND.name)
node3 = node(type_of_node.INPUT.name)
node4 = node(type_of_node.OUTPUT.name)
G = nx.Graph()
G.add_edge(node1, node2)
G.add_edge(node3, node2)
G.add_edge(node4, node2)

nx.draw_spring(G, with_labels = True)
plt.show()