# Define the path to your Python script
$python_script = "Testing_GNN.py"

# Define the file path to be passed to the Python script
$file_path = "test_sample.txt"  # Replace this with the path to your file

# Call the Python script and pass the file path as an argument
$output = & python $python_script $file_path

# Check the output and print "success" or "failure" accordingly
if ($LASTEXITCODE -eq 0) {
    Write-Output "Success : Prediction saved in 'pred.txt'"
} else {
    Write-Output "failure"
}
