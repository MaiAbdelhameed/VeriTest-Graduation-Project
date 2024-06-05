# Define the path to your Python script
$python_script = "Testing_GNN.py"

# Define the file path to be passed to the Python script
$file_path = "test_sample_synth.txt"  # Replace this with the path to your file

# Call the Python script and pass the file path as an argument, redirecting output to pred.txt
& python $python_script $file_path > pred.txt

# Check if the Python script executed successfully
if ($?) {
    Write-Output "Success: Prediction saved in 'pred.txt'"
    return "Success: Prediction saved in 'pred.txt'"
} else {
    Write-Output "Failure"
    return "Failure"
}
