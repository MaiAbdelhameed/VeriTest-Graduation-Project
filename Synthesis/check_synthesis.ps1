# Create folders to store success and failed files
New-Item -ItemType Directory -Path success -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path failed -ErrorAction SilentlyContinue

# Loop through all .v files in the current directory
foreach ($file in Get-ChildItem -Filter "*.v") {

    $filenameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($file)
    # Run quartus_map with the current file
    quartus_map $filenameWithoutExtension --source="$file" --family="Cyclone V"

    # Check the exit code
    if ($LastExitCode -eq 0) {
        # Copy the file to the success folder
        Copy-Item -Path "$file" -Destination success\
    } else {
        # Copy the file to the failed folder
        Copy-Item -Path "$file" -Destination failed\
    }
}
