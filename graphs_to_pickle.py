import sys
from Coverage.coverage import COVERAGE_MAIN
from PARSER.code_to_graph import code_to_graph

import os
import glob
import networkx as nx

files = glob.glob(os.path.join("success", '*'))
    
number_of_files = 0

import shutil
import pickle

for file_path in files:
    print(number_of_files)
    with open(file_path, 'r') as file:
        G = nx.DiGraph()
        try:
            G = code_to_graph(file_path)
        except Exception as e:
            errors_folder = os.path.join(os.getcwd(), 'errors')
            if not os.path.exists(errors_folder):
                os.makedirs(errors_folder)

            
            file.close()
            shutil.copy(file_path, errors_folder)
            with open("errors/"+ file_path[8:], "a") as file2:
                file2.write("\nError occurred: " + str(e))
            file2.close()
            continue
        pickle_file = "PARSED/"+file_path[8:len(file_path)-2] + ".gpickle"

        number_of_files += 1
        with open(pickle_file, 'wb') as f:
            pickle.dump(G, f, pickle.HIGHEST_PROTOCOL)

        


print("finished:", number_of_files ,"out of:", 463,"file")