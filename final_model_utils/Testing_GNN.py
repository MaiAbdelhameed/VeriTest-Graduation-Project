#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[3]:


from GNN_utils import *


# In[4]:


def infer_GNN(test_file):
    
    verilog_file = preprocessing_test(test_file)
    data = extracting_attributes(verilog_file)
    pred_label = get_prediction(data)
    label = get_label_infer(pred_label)
    
    return label


# In[8]:


test_file = 'test_sample.txt'
label = infer_GNN(test_file)
print(label)


# In[9]:


from nbconvert import ScriptExporter

def convert_notebook_to_script(notebook_filename, script_filename):
    exporter = ScriptExporter()
    output, _ = exporter.from_filename(notebook_filename)
    with open(script_filename, 'w') as f:
        f.write(output)

convert_notebook_to_script('Testing_GNN.ipynb', 'Testing_GNN.py')


# In[ ]:




