# Define the path to the Verilog code file
$verilog_file = "verilog_code.v"

# Call the Python script and pass the Verilog code file as an argument
$output = & python encoding_main.py $verilog_file > $null

# Check the output and print "success" or "failed" accordingly
if ($LASTEXITCODE -ne 0) {
    Write-Output "failed"
} else {
    Write-Output "success"
}
