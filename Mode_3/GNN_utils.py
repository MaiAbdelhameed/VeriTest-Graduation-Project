#!/usr/bin/env python
# coding: utf-8


from torch_geometric.nn import SAGEConv
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
import os

# from tensorboardX import SummaryWriter
from sklearn.manifold import TSNE

warnings.filterwarnings("ignore")


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
                data = Data(x=x, edge_index=edge_index, y=y, batch=batch)
                return data

    except Exception as e:
        print(e)
        return e


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
        self.linear = nn.Linear(
            in_features=128, out_features=num_output_classes)

    def forward(self, x, edge_index, batch):

        x = self.gcn1(x, edge_index)
        x = self.r1(x)
        x = self.gcn2(x, edge_index)
        x = self.r2(x)
        x = self.gcn3(x, edge_index)
        # x = self.r3(x)
        # x = self.gcn4(x, edge_index)
        x = global_mean_pool(x, batch)

        x = F.dropout(x, p=0.4, training=self.training)
        x = self.linear(x)

        probs = F.log_softmax(x, dim=-1)

        return probs


        # KNN
        # embeddings
        # PCA
GCN()


def preprocessing_test(test_file):
    if test_file.endswith('.txt'):
        with open(test_file, "r") as file:
            loaded_data = json.load(file)
            return loaded_data


def extracting_attributes(verilog_file):
    try:
        nodes = verilog_file[0]
        edges = verilog_file[1]
        label = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        x = torch.tensor(nodes, dtype=torch.float)
        edge_index = torch.tensor(edges, dtype=torch.long)
        y = torch.tensor(label, dtype=torch.float)
        num_nodes = x.size(0)

        # Create batch assignment vector (assuming one graph per file)
        batch = torch.zeros(num_nodes, dtype=torch.long)
        data = Data(x=x, edge_index=edge_index, y=y, batch=batch)
        return data

    except Exception as e:
        print(e)
        return e


def get_label_infer(pred_label):
    label_mapping = {
        'adder': 0, 'comparator': 1, 'decoder': 2,
        'encoder': 3, 'mult': 4, 'mux': 5, 'pe': 6, 'sub': 7, 'and': 8, 'or': 9, 'not': 10, 'nand': 11, 'nor': 12, 'xnor': 13
    }
    label = [k for k, v in label_mapping.items() if v == pred_label]
    return label[0]


def get_prediction(data):
    VERITEST_directory = os.getenv('VERITEST_HOME')
    gcn = GCN()
    gcn.load_state_dict(torch.load(
        f'{VERITEST_directory}/Mode_3/gcn_model89-72-0001-200.pth'))
    out = gcn(data.x, data.edge_index, data.batch)
    pred = out.argmax(dim=1)  # Use the class with highest probability.
    pred_label = (pred.tolist())[0]
    return pred_label
#!/usr/bin/env python
# coding: utf-8


warnings.filterwarnings("ignore")


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
                data = Data(x=x, edge_index=edge_index, y=y, batch=batch)
                return data

    except Exception as e:
        print(e)
        return e


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


def preprocessing_test(test_file):
    if test_file.endswith('.txt'):
        with open(test_file, "r") as file:
            loaded_data = json.load(file)
            return loaded_data


def extracting_attributes(verilog_file):
    try:
        nodes = verilog_file[0]
        edges = verilog_file[1]
        label = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        x = torch.tensor(nodes, dtype=torch.float)
        edge_index = torch.tensor(edges, dtype=torch.long)
        y = torch.tensor(label, dtype=torch.float)
        num_nodes = x.size(0)

        # Create batch assignment vector (assuming one graph per file)
        batch = torch.zeros(num_nodes, dtype=torch.long)
        data = Data(x=x, edge_index=edge_index, y=y, batch=batch)
        return data

    except Exception as e:
        print(e)
        return e


def get_label_infer(pred_label):
    label_mapping = {
        'Adder': 0, 'Comparator': 1, 'Decoder': 2,
        'Encoder': 3, 'Multiplier': 4, 'Multiplexer': 5, 'Priority Encoder': 6, 'Subtractor': 7,
        'AND Gate': 8, 'OR Gate': 9, 'NOT Gate': 10, 'NAND Gate': 11, 'NOR Gate': 12, 'XNOR Gate': 13, 'XOR Gate': 14}
    label = [k for k, v in label_mapping.items() if v == pred_label]
    return label[0]


def get_prediction(data):
    VERITEST_directory = os.getenv('VERITEST_HOME')

    in_channels = 7
    hidden_channels = 16
    out_channels = 15
    graph_sage = GraphSAGE(in_channels, hidden_channels, out_channels)
    graph_sage.load_state_dict(torch.load(
        f'{VERITEST_directory}/Mode_3/grahpSAGE94_92_200_graph_embeddings.pth'))
    out, _ = graph_sage(data.x, data.edge_index)
    pred = out.argmax(dim=1)  # Use the class with highest probability.
    pred_label = (pred.tolist())[0]
    return pred_label
