from Coverage.coverage import COVERAGE_MAIN
from PARSER.Simulate import PRASER_MAIN
from PARSER.GraphAPI import GraphAPI
from PARSER.code_to_graph import code_to_graph
import networkx as nx
import matplotlib.pyplot as plt
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.REG import REG





G, input_output_wire = code_to_graph("my_module.v")



pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=200, font_size=10, font_color="black")

    # Draw edge labels
edge_labels = {(u, v): f"{G[u][v]['edge_attr'][0].__str__()}" for u, v in G.edges}


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()

API = GraphAPI(G)
x = None



x = COVERAGE_MAIN("my_module.v")


print(x)


        