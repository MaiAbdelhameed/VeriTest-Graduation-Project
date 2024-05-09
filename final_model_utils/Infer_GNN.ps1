# Define the path to your Python script
$python_script = "Testing_GNN.py"

# Define the file path to be passed to the Python script
$file_path = "test_sample.txt"  # Replace this with the path to your file

# Call the Python script and pass the file path as an argument
$output = & python $python_script $file_path

# Save the output (prediction) to a text file
$output | Out-File -FilePath "pred.txt"

# Print a message indicating that the prediction has been saved
Write-Output "Prediction saved to pred.txt"
