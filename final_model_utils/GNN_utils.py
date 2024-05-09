#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import json
import re
import shutil
import torch
import torch.nn.functional as F
import torch_geometric
from torch_geometric.data import Data
import os
import pickle
import json
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import networkx as nx
import matplotlib.pyplot as plt
import warnings
from torch.utils.data import DataLoader, Dataset
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
from torch.utils.data.dataloader import default_collate
from torch.utils.data import random_split
import math
from torch_geometric.utils import to_dense_adj, add_self_loops
from torch_geometric.nn import global_mean_pool
import time
from sklearn.model_selection import train_test_split

# from tensorboardX import SummaryWriter
from sklearn.manifold import TSNE

warnings.filterwarnings("ignore")


# In[5]:


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


# In[6]:


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


# In[7]:


def preprocessing_dataset(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        if not add_label_to_verilog_file(file_path, output_folder):
            print(f"Failed to label: {file_path}")


# In[8]:


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


# In[9]:


def get_files_in_folder(input_folder):
    file_list = []
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list


# In[10]:


# from torch_geometric.nn import GCNConv
class GCN(torch.nn.Module):
    def __init__(self):
        super(GCN, self).__init__()
        
        num_node_features = 20
        num_output_classes = 14
        
        # num_channels = 32
        
        self.gcn1 = GCNConv(num_node_features, 64)
        self.r1 = nn.ReLU()
        self.gcn2 = GCNConv(64, 64)
        self.r2 = nn.ReLU()
        self.gcn3 = GCNConv(64, 128)
        # self.r3 = nn.ReLU()
        # self.gcn4 = GCNConv(128, 128)
        self.linear = nn.Linear(in_features=128, out_features=num_output_classes)

    def forward(self, x, edge_index, batch):
    
        x = self.gcn1(x, edge_index)
        x = self.r1(x)
        x = self.gcn2(x, edge_index)
        x = self.r2(x)
        x = self.gcn3(x, edge_index)
        # x = self.r3(x)
        # x = self.gcn4(x, edge_index)
        x = global_mean_pool(x, batch)
        
        x = F.dropout(x, p = 0.4, training=self.training)
        x = self.linear(x)
        
        probs = F.log_softmax(x, dim=-1)
        
        return probs
        
        
        
        # KNN
        # embeddings
        # PCA
GCN()


# In[11]:


def preprocessing_test(test_file):
    if test_file.endswith('.txt'):
        with open(test_file, "r") as file:
            loaded_data = json.load(file)
            label = label_verilog_file(os.path.basename(test_file))
            if label is not None and [label] not in loaded_data:  # Check if label already exists
                loaded_data.append([label])  # Add label as the third list
            return loaded_data


# In[12]:


def extracting_attributes(verilog_file):
    try:
                nodes = verilog_file[0]
                edges = verilog_file[1]
                label = verilog_file[2]
                
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


# In[13]:


def get_label_infer(pred_label):
    label_mapping = {
        'adder': 0, 'comparator': 1, 'decoder': 2,
        'encoder': 3, 'mult': 4, 'mux': 5, 'pe': 6, 'sub': 7, 'and': 8, 'or': 9, 'not': 10, 'nand': 11, 'nor': 12, 'xnor': 13
    }
    label = [k for k, v in label_mapping.items() if v == pred_label]
    return label[0]


# In[14]:


def get_prediction(data):
    gcn = GCN()
    gcn.load_state_dict(torch.load('gcn_model89-72-0001-200.pth'))
    out = gcn(data.x, data.edge_index, data.batch) 
    pred = out.argmax(dim=1)  # Use the class with highest probability.
    pred_label = (pred.tolist())[0]
    return pred_label


# In[15]:


from nbconvert import ScriptExporter

def convert_notebook_to_script(notebook_filename, script_filename):
    exporter = ScriptExporter()
    output, _ = exporter.from_filename(notebook_filename)
    with open(script_filename, 'w') as f:
        f.write(output)

convert_notebook_to_script('GNN_utils.ipynb', 'GNN_utils.py')


# In[ ]:




