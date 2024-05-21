# Quartus synthesizability check script

# Get the Verilog file path from command-line argument
set verilog_file [lindex $argv 0]

# Set the current directory to where your project files are located
cd {C:\Users\Mai\OneDrive\Documents\GitHub\Verilog-Testbench-Generator-GP\ALU}

# Create a new Quartus project or open an existing one
project_new -overwrite synthesizability_check
project_open synthesizability_check

# Set the family and device
set_global_assignment -name FAMILY "Cyclone V"
set_global_assignment -name DEVICE EP4CE22F17C6

# Add the Verilog file to the project
set_global_assignment -name VERILOG_FILE [file tail $verilog_file]

# Compile the design to check synthesizability
quartus_map --read_settings_files=off --write_settings_files=off synthesizability_check -c $verilog_file
quartus_fit --read_settings_files=off --write_settings_files=off synthesizability_check
quartus_asm --read_settings_files=off --write_settings_files=off synthesizability_check
quartus_sta synthesizability_check

# Close the Quartus project
project_close