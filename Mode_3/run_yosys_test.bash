#!/bin/bash

# Replace 'path_to_python_script.py' with the actual path to your Python script
python_script_path="run_yosys_test.py"

# Execute the Python script with the Verilog file path as an argument
python "$VERITEST_HOME/Mode_3/run_yosys_test.py" "$1" > /dev/null

# Check the exit code of the Python script
if [ $? -eq 0 ]; then
    echo "Yosys synthesis succeeded."
    exit 0
else
    echo "Yosys synthesis failed."
    exit 1
fi
