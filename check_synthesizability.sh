#!/bin/bash

# Path to the folder containing Verilog files
VERILOG_FOLDER="./v_code"

# Iterate through Verilog files in the folder
for FILE in "$VERILOG_FOLDER"/*.v; do
    # echo "hello"
    # Extract file name without extension
    FILENAME=$(basename "$FILE" .v)
    
    # Run Quartus analysis in batch mode
    quartus_map --flow compile "$FILE" -analyze
    
    # Check if any synthesizability issues were reported
    # You may need to adjust this condition based on Quartus output
    if grep -q "synthesizability issue" quartus.log; then
        echo "$FILENAME is not synthesizable"
    else
        echo "$FILENAME is synthesizable"
    fi
done