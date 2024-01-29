from graph import parse_verilog_code
import networkx as nx
import matplotlib.pyplot as plt
from components.INPUT import INPUT

from components.ConstValue import ConstValue
from components.output import OUTPUT
from components.MUX import mux



G, set_of_inputs, set_of_outputs = parse_verilog_code()
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=300, font_size=10, font_color="black", font_weight="bold")

# Draw edge labels
edge_labels = {(u, v): f"{G[u][v]['edge_attr'].__str__()}" for u, v in G.edges}


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()



def finished(set_of_outputs):
    for node in set_of_outputs:
        calculated = node.calculate_output()
        if calculated == False:
            return False
    return True



def isInput(node, nodeadj):
    if isinstance(node, mux):
        for gate in node.G:
            if gate == nodeadj:
                return True
        if nodeadj == node.selector:
            return True

    for gate in node.G:
        if gate == nodeadj:
            return True
        
    return False
    



stack = list()
def DFS(node):
    if node.calculate_output() == False:
        return
    for nodeadj in list(G.neighbors(node)):
        if isinstance(node, OUTPUT) or isInput(node, nodeadj):
            continue

        DFS(nodeadj)


for x in set_of_inputs:
    if not isinstance(x, ConstValue):
        INPUT = input(f"Enter {x.name} ")
        x.connect_input(INPUT)
    



for node in set_of_inputs:
    DFS(node)





for node in G:
    if isinstance(node, OUTPUT):
        node.calculate_output()
        print(f"{node.name}: ","".join(node.output[::-1]))

    
    