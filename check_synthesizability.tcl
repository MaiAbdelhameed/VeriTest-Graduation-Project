load_package flow
# Quartus synthesizability check script

# Get the Verilog file path from command-line argument
set verilog_file [lindex $argv 0]

# Create a new Quartus project
project_new -overwrite synthesizability_check

# Set the family and device

set_global_assignment -name FAMILY "Cyclone IV E"
set_global_assignment -name DEVICE EP4CE22F17C6


project_open synthesizability_check


# Add the Verilog file to the project
# set_full_path $verilog_file
set_global_assignment -name VERILOG_FILE [file tail $verilog_file]


# Compile the design to check synthesizability
# execute_module -tool map
execute_flow -compile

# Close the Quartus project
project_close
