import os
import pickle

# Specify the directory containing the pickle files
folder_path = "./PARSED/ALU10.gpickle"

# Initialize an empty list to store the loaded data from pickle files
data_list = []

# Iterate over each file in the directory
for file_name in os.listdir(folder_path):
    # Check if the file is a pickle file
    if file_name.endswith('.gpickle'):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Open the file in binary read mode
        with open(file_path, 'rb') as f:
            # Load the data from the pickle file
            loaded_data = pickle.load(f)
            data_list.append(loaded_data)

# Now data_list contains the loaded data from all pickle files in the folder
