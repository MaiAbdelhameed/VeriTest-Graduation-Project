#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import re
import shutil
import torch
import torch.nn.functional as F
import torch_geometric
from torch_geometric.data import Data
import pickle
import random
import numpy as np
import torch.nn as nn
import networkx as nx
import matplotlib.pyplot as plt
import warnings
from torch.utils.data import DataLoader, Dataset
from torch_geometric.nn import SAGEConv
from torch.utils.data.dataloader import default_collate
from torch.utils.data import random_split
import math
from torch_geometric.utils import to_dense_adj, add_self_loops
from torch_geometric.nn import global_mean_pool
import time
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


# In[2]:


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


# In[3]:


from torch_geometric.nn import global_mean_pool
class GraphSAGE(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GraphSAGE, self).__init__()
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, out_channels)
        

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        emb = self.conv2(x, edge_index)
        x = global_mean_pool(emb, batch=None)
        return x, emb


# In[4]:


def preprocessing_test(test_file):
    if test_file.endswith('.txt'):
        with open(test_file, "r") as file:
            loaded_data = json.load(file)
            return loaded_data


# In[5]:


def extracting_attributes(verilog_file):
    try:
                nodes = verilog_file[0]
                edges = verilog_file[1]
                label =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                
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


def get_label_infer(pred_label):
    label_mapping = {
        'adder': 0, 'comparator': 1, 'decoder': 2,
        'encoder': 3, 'mult': 4, 'mux': 5, 'pe': 6, 'sub': 7, 'and': 8, 'or': 9, 'not': 10, 'nand': 11, 'nor': 12, 'xnor': 13
    }
    label = [k for k, v in label_mapping.items() if v == pred_label]
    return label[0]


# In[9]:


def get_prediction(data):
    in_channels = 7
    hidden_channels = 16
    out_channels = 15
    graph_sage = GraphSAGE(in_channels, hidden_channels, out_channels)
    graph_sage.load_state_dict(torch.load('grahpSAGE94_92_200_graph_embeddings.pth'))
    out,_ = graph_sage(data.x, data.edge_index) 
    pred = out.argmax(dim=1)  # Use the class with highest probability.
    pred_label = (pred.tolist())[0]
    return pred_label


# In[10]:


from nbconvert import ScriptExporter

def convert_notebook_to_script(notebook_filename, script_filename):
    exporter = ScriptExporter()
    output, _ = exporter.from_filename(notebook_filename)
    with open(script_filename, 'w') as f:
        f.write(output)

convert_notebook_to_script('GNN_utils.ipynb', 'GNN_utils.py')


# In[ ]:




