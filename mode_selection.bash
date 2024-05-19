#!/bin/bash


# make absolute path function

make_absolute_path() {
    local path="$1"
    if [[ "${path:0:1}" != "/" ]]; then
        path="$(pwd)/$path"  # prepend current directory
    fi
    echo "$path"
}



# Check if there are exactly two command line arguments
if [ "$#" -ne 2 ]; then
    echo "Incorrect number of arguments. Exiting."
    exit 1
fi

# choose mode 1 or mode 2
# Mode 1
if [[ "$1" == *.v && "$2" == *.py ]]; then
    # mode 1 -> code.v / code.py
    echo "Mode 1: .v and .py files"
    
    
    # getting absolute file path
    verilog_file_path="$1"
    python_file_path="$2"
    verilog_absolute_path=$(make_absolute_path "$verilog_file_path")
    python_absolute_path=$(make_absolute_path "$python_file_path")
    
    
    
    
    bash "$VERITEST_HOME/main.sh" "${verilog_absolute_path}"
    
    # Mode 2
    elif [[ "$1" == *.v && "$2" == *.json ]]; then
    # mode 2 -> code.v / code.json
    echo "Mode 2: .v and .json files"
    
    # getting absolute file path
    verilog_file_path="$1"
    json_file_path="$2"
    verilog_absolute_path=$(make_absolute_path "$verilog_file_path")
    json_absolute_path=$(make_absolute_path "$json_file_path")
    
    
    
    
    bash "$VERITEST_HOME/Mode_2/mode2.bash" "${verilog_absolute_path}"
    
    
else
    echo "Arguments don't match any supported modes. Exiting."
    exit 1
fi




