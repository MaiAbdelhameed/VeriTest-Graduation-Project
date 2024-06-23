#!/bin/bash



# Define the file path to be passed to the Python script
file_path="test_sample_synth.txt"  # Replace this with the path to your file

# Call the Python script and pass the file path as an argument, redirecting output to pred.txt

prediction=$(python $VERITEST_HOME/Mode_3/Testing_GNN.py)
path=$1
original_filename="${path/_synth.v/.v}"
python $VERITEST_HOME/Mode_3/generate_json.py $original_filename $prediction
# Check if the Python script executed successfully
if [[ $? -eq 0 ]]; then
    echo "Success: Prediction saved in 'pred.txt'"
    exit 0
else
    echo "Failure"
    exit 1
fi
