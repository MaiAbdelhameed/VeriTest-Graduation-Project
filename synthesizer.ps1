param (
    [string]$source_folder = "success_1",  # Define the source folder containing Verilog files
    [string]$fail_folder = "synthesis_fails"   # Define the folder for files that fail synthesis
)

# Ensure the fail folder exists
if (-not (Test-Path -Path $fail_folder)) {
    New-Item -ItemType Directory -Path $fail_folder
}

# Log file for failed files
$log_file = Join-Path $fail_folder "synthesis_fails_log.txt"
if (Test-Path -Path $log_file) {
    Remove-Item -Path $log_file  # Remove existing log file if it exists
}

# Get all Verilog files in the source folder
$verilog_files = Get-ChildItem -Path $source_folder -Filter *.v

foreach ($file in $verilog_files) {
    $verilog_file = $file.FullName
    $filenameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($verilog_file)
    $output = & quartus_map $filenameWithoutExtension --source="$verilog_file" --family="Cyclone V" 2>&1

    # Check if the output contains compilation errors or synthesizability indicators
    $compilationErrors = $output -match "Error:" -or $output -match "Fatal Error:"
    $synthesizabilityIssues = $output -match "Critical Warning:"

    # Determine the result based on the presence of compilation errors and synthesizability issues
    if ($compilationErrors -or $synthesizabilityIssues) {
        # If the file has errors or issues, move it to the fail folder
        Move-Item -Path $verilog_file -Destination $fail_folder
        
        # Determine the reason for failure
        $failureReason = ""
        if ($compilationErrors) {
            $failureReason += "Compilation Error"
        }
        if ($synthesizabilityIssues) {
            if ($failureReason) {
                $failureReason += " and "
            }
            $failureReason += "Synthesizability Issue"
        }

        # Write the failed file name and reason to the log file
        $logEntry = "$verilog_file : $failureReason"
        Add-Content -Path $log_file -Value $logEntry
    }
}
