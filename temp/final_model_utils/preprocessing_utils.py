#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import re
import shutil
import torch
import torch.nn.functional as F
get_ipython().run_line_magic('pip', 'install torch_geometric -q')
import torch_geometric
from torch_geometric.data import Data


# In[2]:


def label_verilog_file(file_name):
    
    ground_truth_labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] # no xor , no ALU
    labels_torch = torch.tensor(ground_truth_labels)

    # One-hot encode the labels
    one_hot_labels = F.one_hot(labels_torch, num_classes=14)


    label_mapping = {
        'adder': 0, 'comparator': 1, 'decoder': 2,
        'encoder': 3, 'mult': 4, 'mux': 5, 'pe': 6, 'sub': 7, 'and': 8, 'or': 9, 'not': 10, 'nand': 11, 'nor': 12, 'xnor': 13
    }
    
    pattern = r"([a-zA-Z]+)(\d+)?"
    match = re.match(pattern, file_name)
    if match:
        base_name = match.group(1)
        if base_name in label_mapping:
            return one_hot_labels[label_mapping[base_name]].tolist()
        
    return None


# In[3]:


def add_label_to_verilog_file(input_file_path, output_folder):
    if input_file_path.endswith('.txt'):
        with open(input_file_path, "r") as file:
            loaded_data = json.load(file)
            label = label_verilog_file(os.path.basename(input_file_path))
            if label is not None and [label] not in loaded_data:  # Check if label already exists
                loaded_data.append([label])  # Add label as the third list
                output_file_path = os.path.join(output_folder, os.path.basename(input_file_path))
                with open(output_file_path, "w") as output_file:
                    json.dump(loaded_data, output_file)
                return True
    return False


# In[4]:


def preprocessing_dataset(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        if not add_label_to_verilog_file(file_path, output_folder):
            print(f"Failed to label: {file_path}")


# In[5]:


def extracting_attributes(verilog_file):
    try:
        if os.path.isfile(verilog_file):
            with open(verilog_file, "r") as file:
                
                loaded_data = json.load(file)
                print(loaded_data)
                nodes = loaded_data[0]
                edges = loaded_data[1]
                label = loaded_data[2]
                
                x = torch.tensor(nodes, dtype=torch.float)
                edge_index = torch.tensor(edges, dtype=torch.long)
                y = torch.tensor(label, dtype=torch.float)
                num_nodes = x.size(0)
                
                # Create batch assignment vector (assuming one graph per file)
                batch = torch.zeros(num_nodes, dtype=torch.long)
                data = Data(x=x, edge_index=edge_index, y = y, batch = batch)
                return data
    
    except Exception as e:
        print(e)
        return e


# In[6]:


def get_files_in_folder(input_folder):
    file_list = []
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list


# In[7]:


def create_py():
    get_ipython().system('jupyter nbconvert --to script preprocessing_utils.ipynb')


if __name__ == '__main__':
    create_py()


# In[ ]:




