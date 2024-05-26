import os

def replace_not_in_file(file_path):
    # Open the file for reading and writing
    with open(file_path, 'r+') as file:
        # Read the file content
        content = file.read()
        
        # Replace 'NOT' with 'not'
        updated_content = content.replace('NOT', 'not')
        
        # Move the file cursor to the beginning of the file
        file.seek(0)
        # Write the updated content to the file
        file.write(updated_content)
        # Truncate the file to the new length
        file.truncate()

def check_for_reg_keyword(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the file content
        content = file.read()
        
        # Check if 'REG' is in the content
        if 'REG' in content:
            print(f"File {file_path} contains the keyword 'REG'.")

def process_files_in_directory(directory_path):
    # Loop over all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # Check if the file has a .v extension
            if file_name.endswith('.v'):
                file_path = os.path.join(root, file_name)
                
                # Call the function to replace 'NOT' with 'not'
                replace_not_in_file(file_path)
                
                # Check if the file contains the keyword 'REG'
                check_for_reg_keyword(file_path)
                
                # print(f"Processed file: {file_path}")

if __name__ == "__main__":
    # Path to the directory
    directory_path = './yosys_files'
    
    # Call the function to process all .v files in the directory
    process_files_in_directory(directory_path)
