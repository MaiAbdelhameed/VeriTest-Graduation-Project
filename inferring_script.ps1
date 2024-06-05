$verilog_file = "test_sample.v"
# Call synthesizer.ps1 with the Verilog file
$synthesizer_output = .\synthesizer.ps1 $verilog_file

# Check for failure in synthesizer.ps1
if ($synthesizer_output -eq "compilation failed" -or $synthesizer_output -eq "synthesizability check failed") {
    Write-Host "Synthesizer failed: $synthesizer_output"
    return $synthesizer_output
}


# Call run_yosys_test.ps1 with the Verilog file as an argument
.\run_yosys_test.ps1

# Check for failure in run_yosys_test.ps1
# Check the exit code of the Python script
if ($LASTEXITCODE -eq 1) {
    Write-Host "Yosys synthesis failed."
    return "failure"
}


$verilog_file = "test_sample_synth.v"

# Call encode_test_sample.ps1 with the Verilog file as an argument
$encode_output = .\encode_test_sample.ps1 -verilog_file $verilog_file

# Check for failure in encode_test_sample.ps1
if ($encode_output -ne "success") {
    Write-Host "Encoding failed: $encode_output"
    return "Encoding failed"
}

# Change directory to the "final_model_utils" folder
Set-Location -Path "final_model_utils"

# Call Infer_GNN.ps1
$infer_output = .\Infer_GNN.ps1

# Check for failure in Infer_GNN.ps1
if ($infer_output -ne "Success: Prediction saved in 'pred.txt'") {
    Write-Host "Inference failed: $infer_output"
    return "Inference failed"
}

# If all steps succeeded, return success
return "Success : Prediction saved in 'pred.txt'"
