from graph import parse
import networkx as nx
import matplotlib.pyplot as plt
from components.Gate import gate
from components.INPUT import Input

from components.Wire import wire
from components.OUTPUT import Output



G, set_of_inputs, set_of_outputs = parse()

def finished(set_of_outputs):
    for node in set_of_outputs:
        node.calculate_output()
        for bit in node.output:
            if bit == None:
                return False
    return True




stack = list()
def DFS(node):

    if node.calculate_output() == False:
        return
    for nodeadj in list(G.neighbors(node)):
        if isinstance(node, Output):
            continue
        if node.G1 == nodeadj or node.G2 == nodeadj:
            continue
        DFS(nodeadj)


for x in set_of_inputs:
    INPUT = input(f"Enter {x.name} ")
    x.connect_input(INPUT)
    


while not finished(set_of_outputs):
    for node in set_of_inputs:
        DFS(node)


for node in G:
    if isinstance(node, Output):
        node.calculate_output()
        print("".join(node.output))

    
    