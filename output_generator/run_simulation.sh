#!/bin/bash

# Run vlog command on the file


if [ -e "$1" ]; then
    cp "$1" "./results"
else
    echo "File $1 does not exist. Stopping the script."
    exit 1
fi


cd "results"

vlog "generated_tb.v"

# Check the exit status of the vlog command
# if [ $? -eq 0 ]; then
#     echo "vlog succeeded"
#     vlog "$(basename "$1")"
#     vsim tb

# else
#     echo "vlog failed"

# fi

cd ..

