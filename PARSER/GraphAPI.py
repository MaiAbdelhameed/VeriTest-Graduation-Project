from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT
from PARSER.components.IN_OUT_WIRE.WIRE import wire
from PARSER.components.IN_OUT_WIRE.REG import REG
from PARSER.components.Gates.ConstValue import ConstValue
from PARSER.connection import connection
import re

class GraphAPI:

    def __init__(self, G):
        self.G = G
    

    def calc_output(self, dict_of_cases):
        return self.simulate(dict_of_cases)

    def search_for_connection(self, node, nodeadj, G):
        edges = G.edges[node, nodeadj]["edge_attr"]
        return edges

    def all_outputs_calcualted(self, G):
        for node in G.nodes():
            if isinstance(node, OUTPUT) or isinstance(node, wire) or isinstance(node, REG):
                if "X" in node.output:
                    return False
        return True


    def DFS(self, node, G):
        for nodeadj in list(G.neighbors(node)):
            connection = self.search_for_connection(node, nodeadj, G)
            state = node.process_node(connection)
            if state == True and not self.all_outputs_calcualted(G):
                self.DFS(nodeadj, G)
            else:
                continue
                
        

    def simulate(self, dict_of_cases):
        number_of_test_cases = len(dict_of_cases[list(dict_of_cases.keys())[0]])
        dict_of_wires_outputs = dict()
        G2 = self.G.copy()
        DFS_START = list()
        for node in G2.nodes():
            if isinstance(node, INPUT):
                #user_input = re.search("(?<=b)\d+", dict_of_cases[node.name][index]).group(0)
                const_node = ConstValue()
                const_node.name = node.name
                self.G.add_node(const_node)
                connecting_edge = connection()
                connecting_edge.source = const_node
                connecting_edge.destination = node
                const_node.add_connection(connecting_edge)
                node.add_connection(connecting_edge)
                DFS_START.append(const_node)
                edge_attr = list()
                edge_attr.append(connecting_edge)
                self.G.add_edge(const_node, node, edge_attr = edge_attr)
            elif isinstance(node, ConstValue):
                DFS_START.append(node)
            
            elif isinstance(node, OUTPUT) or isinstance(node, wire) or isinstance(node, REG):
                dict_of_wires_outputs.update({node.name: list()})
        

        

        for index in range(number_of_test_cases):
            for node in DFS_START:
                if node.name != None:
                    try:
                        node.output = re.search("(?<=b)\d+", dict_of_cases[node.name][index]).group(0)
                    except:
                        node.output = ""
                self.DFS(node, self.G)




            for node in self.G:
                if isinstance(node, OUTPUT) or isinstance(node, wire) or isinstance(node, REG):
                    if len(node.output) < node.size:
                        if node.endian == "little":
                            node.output = (["X"] * abs(len(node.output)- node.size)) + node.output
                        else:
                            node.output = node.output + (["X"] * abs(len(node.output)- node.size))
                    dict_of_wires_outputs[node.name].append("".join(node.output))

        return dict_of_wires_outputs

       