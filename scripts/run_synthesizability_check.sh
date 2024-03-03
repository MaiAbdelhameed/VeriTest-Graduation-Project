
echo "hello"

CURRENT_DIR=$(pwd)

# Set the path to Quartus Prime installation directory
QUARTUS_INSTALL_DIR="C:/intelFPGA_lite/18.1/quartus"

# Set the directory containing Verilog files
VERILOG_DIR="${CURRENT_DIR}/v_code"

# Path to Quartus Tcl script
TCL_SCRIPT="${CURRENT_DIR}/check_synthesizability.tcl"


#Navigate to the Quartus installation directory
cd "$QUARTUS_INSTALL_DIR"

# Run Quartus Tcl script for each Verilog file
for file in "$VERILOG_DIR"/*.v; do
    # Extract only the filename without the path and extension
    filename=$(basename -- "$file")
    filename_no_ext="${filename%.*}"
    
    # Run Quartus Tcl script to check synthesizability
    quartus_sh -t "$TCL_SCRIPT" "$file" > "${CURRENT_DIR}/outputs/$filename_no_ext.log"
done
