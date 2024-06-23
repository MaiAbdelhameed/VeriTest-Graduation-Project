from PARSER.graph import parse_verilog_code
import networkx as nx
import matplotlib.pyplot as plt
from PARSER.components.Gates.ConstValue import ConstValue
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
# from PARSER.connection import connection
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
import os


def code_to_graph(file_path):  # shelt el PARSER/files/ hna
    HOME = os.environ.get('VERITEST_HOME')
    top_level_entity_file = f"{HOME}/PARSER/files/" + file_path
    print(top_level_entity_file)
    G, _, input_out_wire = parse_verilog_code(
        top_level_entity_file, top_level=True)

    return G, input_out_wire
