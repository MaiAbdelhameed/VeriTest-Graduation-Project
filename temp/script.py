import os

# Path to the folder containing Verilog files
input_folder_path = "C:/Users/Mai/OneDrive/Documents/GitHub/Verilog-Testbench-Generator-GP/temp/temp_mux"
output_folder_path = "C:/Users/Mai/OneDrive/Documents/GitHub/Verilog-Testbench-Generator-GP/temp/output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Define the range of indices for renaming
start_index = 27
end_index = 77

# Loop over each Verilog file in the input folder
for index in range(1, 51):
    old_file_name = f"m{index}.v"
    new_file_name = f"mux{start_index}.v"
    old_module_name = f"old_module_name"
    new_module_name = f"mux{start_index}"
    
    # input_file_path = os.path.join(input_folder_path, old_file_name)
    # output_file_path = os.path.join(output_folder_path, new_file_name)
    
    input_file_path = input_folder_path + "/" + old_file_name
    output_file_path = output_folder_path + "/" + new_file_name
    # print(input_file_path)
    # print(output_file_path)
    # break
    
    # Check if the file exists
    if os.path.exists(input_file_path):
        # Open the input file and read its contents
        with open(input_file_path, "r") as input_file:
            content = input_file.read()
        
        # Replace the module name with the new name
        new_content = content.replace(old_module_name, new_module_name)
        
        # Write the modified content to the output file in the adjusted folder
        with open(output_file_path, "w") as output_file:
            output_file.write(new_content)
            
        print(f"File '{old_file_name}' adjusted and saved as '{new_file_name}' in the 'adjusted' folder.")
        
        # Increment start_index for the next file
        start_index += 1
    else:
        print(f"File '{old_file_name}' does not exist in the input folder.")
