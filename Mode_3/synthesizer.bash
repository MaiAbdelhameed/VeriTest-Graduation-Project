#!/bin/bash

# Define the Verilog file path as a command-line argument
verilog_file="$1"

# Check if the file path is provided
if [[ -z "$verilog_file" ]]; then
    echo "Error: No Verilog file path provided."
    exit 1
fi

# Get the filename without the extension
filenameWithoutExtension=$(basename "$verilog_file" .v)

# Run quartus_map with the given file
output=$(quartus_map "$filenameWithoutExtension" --source="$verilog_file" --family="Cyclone V" 2>&1)

# Check if the output contains compilation errors or synthesizability indicators
compilationErrors=$(echo "$output" | grep -E "Error:|Fatal Error:")
synthesizabilityIssues=$(echo "$output" | grep "Critical Warning:")

# Determine the result based on the presence of compilation errors and synthesizability issues
if [[ -n "$compilationErrors" && -n "$synthesizabilityIssues" ]]; then
    # Both compilation errors and synthesizability issues found
    echo "Compilation and Synthesizability Check Failed"
    exit 1
    elif [[ -n "$compilationErrors" ]]; then
    # Only compilation errors found
    echo "Compilation Failed"
    exit 1
    elif [[ -n "$synthesizabilityIssues" ]]; then
    # Only synthesizability issues found
    echo "Synthesizability Check Failed"
    exit 1
else
    # No errors found, both checks succeeded
    echo "Compilation and Synthesizability Check Succeeded"
    exit 0
fi
