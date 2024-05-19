param (
    [string]$verilog_file  # Define the Verilog file name as a command-line argument
)

# Run quartus_map with the given file
$filenameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($verilog_file)
$output = & quartus_map $filenameWithoutExtension --source="$verilog_file" --family="Cyclone V" 2>&1

# Check if the output contains compilation errors or synthesizability indicators
$compilationErrors = $output -match "Error:" -or $output -match "Fatal Error:"
$synthesizabilityIssues = $output -match "Critical Warning:"

# Determine the result based on the presence of compilation errors and synthesizability issues
if ($compilationErrors -and $synthesizabilityIssues) {
    # Write-Host "Compilation and synthesizability check failed for $verilog_file"
    # Write-Host "Error output: $output"
    return "Compilation and Synthesizability Check Failed"
} elseif ($compilationErrors) {
    # Write-Host "Compilation failed for $verilog_file"
    # Write-Host "Error output: $output"
    return "Compilation Failed"
} elseif ($synthesizabilityIssues) {
    # Write-Host "Synthesizability check failed for $verilog_file"
    # Write-Host "Error output: $output"
    return "Synthesizability Check Failed"
} else {
    # Write-Host "Compilation and synthesizability check succeeded for $verilog_file"
    return "Compilation and Synthesizability Check Succeeded"
}
