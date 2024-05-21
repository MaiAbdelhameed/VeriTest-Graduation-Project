import os
import re

# Function to rename module name in Verilog file
def rename_module(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Extracting module name from filename
    module_name = os.path.splitext(os.path.basename(filename))[0]

    # Replacing module name in content
    new_content = re.sub(r'module\s+(\w+)\s*\(', r'module ' + module_name + ' (', content)

    # Writing modified content back to file
    with open(filename, 'w') as file:
        file.write(new_content)

# Function to loop over Verilog files in a folder and rename module names
def rename_modules_in_folder(folder):
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.v'):
                filepath = os.path.join(root, filename)
                rename_module(filepath)

# Example usage
folder_path = 'C:/Users/Mai/OneDrive/Documents/GitHub/Verilog-Testbench-Generator-GP/Combinational/Binary_BCD'
rename_modules_in_folder(folder_path)
