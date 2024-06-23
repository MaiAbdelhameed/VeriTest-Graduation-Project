#!/bin/bash

# Define the Verilog file path as a command-line argument
verilog_file="$1"

# Check if the file path is provided
if [[ -z "$verilog_file" ]]; then
    echo "Error: No Verilog file path provided."
    exit 1
fi

# Call the Python script and pass the Verilog code file as an argument
python "${VERITEST_HOME}/Mode_3/encoding_main.py" "$verilog_file"

# Check the exit code of the Python script
if [[ $? -ne 0 ]]; then
    echo "failure"
    exit 1
else
    echo "success"
    exit 0
fi
