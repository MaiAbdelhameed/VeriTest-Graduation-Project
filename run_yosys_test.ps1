# Replace 'path_to_python_script.py' with the actual path to your Python script
$python_script_path = "run_yosys_test.py"



# Execute the Python script with the Verilog file path as argument
python $python_script_path 

# Check the output of the Python script
# Check the exit code of the Python script
if ($LASTEXITCODE -eq 0) {
    Write-Host "Yosys synthesis succeeded."
    # Write-Host "Suceess ya mai"
    exit 0
} else {
    Write-Host "Yosys synthesis failed."
    exit 1 
}