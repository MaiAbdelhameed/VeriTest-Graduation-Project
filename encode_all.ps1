# Change directory to "success"
Set-Location -Path "success_new"

$failed_count = 0
$done_files = 0
$file_count = (Get-ChildItem -File).Count

# Iterate over each file in the directory
foreach ($file in Get-ChildItem -File) {
    # Run main.py with the file name as the command-line argument
    python ../final_model_utils/main.py $file.Name > $null

    # Check the exit status of the previous command
    if ($LASTEXITCODE -ne 0) {
        # Increment the counter and print the name of the failed file
        $failed_count++
        Write-Host "Failed: $($file.FullName)"
        $file.FullName >> "failed_files.txt"
    }

    $done_files++
    Write-Host "$done_files/$file_count"
}

Write-Host "Total failed files: $failed_count"
