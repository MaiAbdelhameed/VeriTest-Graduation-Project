import json


def read_file(file_path):
    with open(file_path, "r") as file:
        loaded_data = json.load(file)
    
    nodes = loaded_data[0]
    edges = loaded_data[1]

    return nodes, edges

# nodes, edges = read_file("encoded/adder11.txt")
# print(nodes)
# print(edges)