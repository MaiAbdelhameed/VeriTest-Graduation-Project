# echo "hello"
Write-Host "hello"

# Get the current directory
$CURRENT_DIR = Get-Location

# Set the path to Quartus Prime installation directory
$QUARTUS_INSTALL_DIR = "C:/intelFPGA_lite/18.1/quartus"

# Set the directory containing Verilog files
$VERILOG_DIR = Join-Path $CURRENT_DIR "ALU"

# Path to Quartus Tcl script
$TCL_SCRIPT = Join-Path $CURRENT_DIR "check_synthesizability.tcl"

# Navigate to the Quartus installation directory
# Set-Location -Path $QUARTUS_INSTALL_DIR

# Run Quartus Tcl script for each Verilog file
foreach ($file in Get-ChildItem -Path $VERILOG_DIR -Filter *.v) {
    # Extract only the filename without the path and extension
    $filename = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    
    # Run Quartus Tcl script to check synthesizability
    quartus_sh -t $TCL_SCRIPT $file 
}