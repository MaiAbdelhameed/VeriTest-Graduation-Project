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
import math


if len(sys.argv) < 2:
    print("Usage: python main.py <argument>")
    sys.exit(1)

filename = sys.argv[1]
prediction = sys.argv[2].lower()
# filename = "my_module.v"

print("JSON DONE")
G, input_output_wire = code_to_graph(filename)


input_variables = input_output_wire[0]
output_variables = input_output_wire[1]


output_json = {}
base_name = os.path.basename(filename)
filename, _ = os.path.splitext(base_name)
output_json["model_name"] = os.path.basename(filename)
output_json["type"] = prediction

if (prediction != "not"):
    output_json["inputs"] = [{'name': name, 'size': size}
                             for name, size in input_variables.items()]

###################################################################
if (prediction in ['and', 'or', 'xor', 'nand', 'nor', 'xnor']):
    output_json["output"] = list(output_variables.keys())[0]
    output_json["operation_type"] = "bitwise"
###################################################################
elif (prediction in ["decoder", "encoder", "seg"]):
    output_json["input_mode"] = "concatenated"
    output_json["output_mode"] = "concatenated"
    output_json["output"] = [{'name': name, 'size': size}
                             for name, size in output_variables.items()]
###################################################################
elif (prediction in ["mux", "adder"]):
    if (prediction == "adder"):
        output_json["mode"] = "unsigned"
    elif (prediction == "mux"):
        output_json["input_mode"] = "concatenated"
        output_json["output_mode"] = "concatenated"

    first_key, first_value = list(output_variables.items())[0]
    output_json["output"] = {'name': first_key, 'size': first_value}
elif (prediction == "not"):
    output_json["inputs_outputs"] = []
    loop_size = min(len(list(output_variables.items())),
                    len(list(input_variables.items())))
    for i in range(0, loop_size):
        input_key, input_value = list(input_variables.items())[i]
        output_key, output_value = list(output_variables.items())[i]
        result_dict = {"input_name": input_key, "output_name": output_key, "size": min(
            input_value, output_value)}
        output_json["inputs_outputs"].append(result_dict)


Veritest_Home = os.environ.get("VERITEST_HOME")

file_path = os.path.join(
    f"{Veritest_Home}/web_portal/backend/uploaded_files", "predicted.json")

# Write the dictionary to a JSON file

with open(file_path, "w") as json_file:
    json.dump(output_json, json_file, indent=4)
print(output_json)
