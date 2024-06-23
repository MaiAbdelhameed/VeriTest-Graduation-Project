
from GNN_utils import *
import os


def infer_GNN(test_file):

    verilog_file = preprocessing_test(test_file)
    data = extracting_attributes(verilog_file)
    pred_label = get_prediction(data)
    label = get_label_infer(pred_label)

    return label


HOME = os.environ.get('VERITEST_HOME')
directory = f'{HOME}/web_portal/backend'
test_file = f'{directory}/final_model_utils/test_sample_synth.txt'
label = infer_GNN(test_file)
print(label)
