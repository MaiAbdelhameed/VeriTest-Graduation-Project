param (
    [string]$verilog_file  # Define the Verilog file name as a command-line argument
)

# Call the Python script and pass the Verilog code file as an argument
$output = & python encoding_main.py $verilog_file > $null

# Check the output and print "success" or "failure" accordingly
if ($LASTEXITCODE -ne 0) {
    # Write-Output "failure"
    return "failure"
} else {
    # Write-Output "success"
    return "success"
}
