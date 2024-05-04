from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import Assign, Concat, And, Xor, Variable, Value, Partselect
from components.INPUT import Input
import networkx as nx
import matplotlib.pyplot as plt

def get_assignments(node):
    assignments = []

    if isinstance(node, Assign):
        # Add the assignment to the list
        assignments.append(node)

    # Recursively visit child nodes
    for child in node.children():
        assignments.extend(get_assignments(child))

    return assignments

def parse_verilog(file_path):
    # Parse the Verilog code
    ast, _ = parse([file_path])

    # Get all assignment statements from the AST
    assignments = get_assignments(ast)

    return assignments

if __name__ == "__main__":
    verilog_file = "module.v"
    assignments = parse_verilog(verilog_file)
    G = nx.Graph()

    # Print the assignment statements
    for assignment in assignments:
        left = assignment.left.var
        right = assignment.right.var
        node = None
        if isinstance(left, Partselect):
            pass
        else:
            node = Input(name=left.name, start=0, end=5, size = 0, Type="OUTPUT")

        

        G.add_node(node)
            
    

    nx.draw_spring(G, with_labels = True)
    # plt.show()


   