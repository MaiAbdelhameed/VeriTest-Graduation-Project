import networkx as nx
import matplotlib.pyplot as plt
from test_class import test_class

# Create a directed graph
G = nx.DiGraph()

# Add edges with two attributes
G.add_edge('Node1', 'Node2', start=test_class('Node1',0,3), end=test_class('Node2',3,5))


# Draw the graph
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")

# Draw edge labels
edge_labels = {(u, v): f"{G[u][v]['start'].__str__()}, {G[u][v]['end'].__str__()}" for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

for node in G.nodes():
    for nodeadj in list(G.neighbors(node)):
        edge_data = G.get_edge_data(node, nodeadj)
        pass

# Show the plot
plt.show()
