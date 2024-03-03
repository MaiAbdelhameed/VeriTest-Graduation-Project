# Initialize counters
$successful_count = 0
$failed_count = 0

# Create directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "successful"

# Loop through each file in the v_code directory
foreach ($file in Get-ChildItem -Path "v_code") {
    # Check if the item is a file
    if ($file.PSIsContainer -eq $false) {
        # Run vlog command on the file
        & vlog $file.FullName
        
        # Check the exit code of the vlog command
        if ($LASTEXITCODE -eq 0) {
            Write-Host "vlog succeeded for $($file.FullName)"
            $successful_count++
            
            # Copy successful file to the 'successful' directory
            Copy-Item -Path $file.FullName -Destination "successful/"
        }
        else {
            Write-Host "vlog failed for $($file.FullName)"
            $failed_count++
        }
    }
}

# Display summary
Write-Host "Total successful: $successful_count"
Write-Host "Total failed: $failed_count"