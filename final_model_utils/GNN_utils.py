#!/usr/bin/env python
# coding: utf-8

# In[32]:


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


# In[35]:


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


# In[37]:


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


# In[38]:


def preprocessing_test(test_file):
    if test_file.endswith('.txt'):
        with open(test_file, "r") as file:
            loaded_data = json.load(file)
            return loaded_data


# In[45]:


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


# In[46]:


def get_label_infer(pred_label):
    label_mapping = {
        'adder': 0, 'comparator': 1, 'decoder': 2,
        'encoder': 3, 'mult': 4, 'mux': 5, 'pe': 6, 'sub': 7, 'and': 8, 'or': 9, 'not': 10, 'nand': 11, 'nor': 12, 'xnor': 13
    }
    label = [k for k, v in label_mapping.items() if v == pred_label]
    return label[0]


# In[47]:


def get_prediction(data):
    gcn = GCN()
    gcn.load_state_dict(torch.load('gcn_model89-72-0001-200.pth'))
    out = gcn(data.x, data.edge_index, data.batch) 
    pred = out.argmax(dim=1)  # Use the class with highest probability.
    pred_label = (pred.tolist())[0]
    return pred_label


# In[48]:


from nbconvert import ScriptExporter

def convert_notebook_to_script(notebook_filename, script_filename):
    exporter = ScriptExporter()
    output, _ = exporter.from_filename(notebook_filename)
    with open(script_filename, 'w') as f:
        f.write(output)

convert_notebook_to_script('GNN_utils.ipynb', 'GNN_utils.py')


# In[ ]:




