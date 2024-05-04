from PARSER.graph import parse_verilog_code
import networkx as nx
import matplotlib.pyplot as plt
from PARSER.components.Gates.ConstValue import ConstValue
from PARSER.components.IN_OUT_WIRE.OUTPUT import OUTPUT
from PARSER.connection import connection
from PARSER.components.IN_OUT_WIRE.INPUT import INPUT

def PRASER_MAIN(file_path):
    #top_level_entity_file = input("Enter top level entity file name: ")
    top_level_entity_file = "PARSER/files/" + file_path
    print(top_level_entity_file)
    G, _ = parse_verilog_code(top_level_entity_file, top_level = True)

    

    # for node in G.nodes():
    #     pass
    pos = nx.spring_layout(G)  # Layout algorithm
    nx.draw(G, pos, with_labels=True, node_size=200, font_size=10, font_color="black")

    # Draw edge labels
    edge_labels = {(u, v): f"{G[u][v]['edge_attr'][0].__str__()}" for u, v in G.edges}


    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # plt.show()



   

    def search_for_connection(node, nodeadj, G):
        edges = G.edges[node, nodeadj]["edge_attr"]
        return edges
        

        
        

    def all_outputs_calcualted(G):
        for node in G.nodes():
            if isinstance(node, OUTPUT):
                if "X" in node.output:
                    return False
        return True


    def DFS(node, G):
        for nodeadj in list(G.neighbors(node)):
            connection = search_for_connection(node, nodeadj, G)
            state = node.process_node(connection)
            if state == True and not all_outputs_calcualted(G):
                DFS(nodeadj, G)
            else:
                continue
                
        

    DFS_START = list()
    G2 = G.copy()

    for node in G2.nodes():
        if isinstance(node, INPUT) and node.istoplevel == True:
            user_input = input(f"Enter {node.name} ")
            const_node = ConstValue(str(user_input))
            G.add_node(const_node)
            connecting_edge = connection()
            connecting_edge.source = const_node
            connecting_edge.destination = node
            const_node.add_connection(connecting_edge)
            node.add_connection(connecting_edge)
            DFS_START.append(const_node)
            edge_attr = list()
            edge_attr.append(connecting_edge)
            G.add_edge(const_node, node, edge_attr = edge_attr)
        elif isinstance(node, ConstValue):
            DFS_START.append(node)
        

        


    for node in DFS_START:
        DFS(node, G)




    for node in G:
        if isinstance(node, OUTPUT) and node.istoplevel == True:
            if len(node.output) < node.size:
                if node.endian == "little":
                    node.output = (["X"] * abs(len(node.output)- node.size)) + node.output
                else:
                    node.output = node.output + (["X"] * abs(len(node.output)- node.size))
            print(node.name, "".join(node.output))

            

          

    return top_level_entity_file

    
    