import os
import sys
import subprocess
import time
import signal

MAXTIMEOUT = 30
# argv[1] is the library name

current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir))
yosys_suite_path = os.path.join(project_dir, 'oss-cad-suite')
print(yosys_suite_path)

os.chdir(yosys_suite_path)

verilog_files_dir = os.path.join(current_dir, 'success_new')


if not os.path.exists(verilog_files_dir):
    print("No verilog files found")
    sys.exit(1)


verilog_files = [f for f in os.listdir(verilog_files_dir) if f.endswith('.v')]

lib_file_path = "C:\\Users\\Mai\\OneDrive\\Documents\\GitHub\\Verilog-Testbench-Generator-GP\\gate.lib"

netlist_files_dir = os.path.join(current_dir, 'yosys_files')

if not os.path.exists(netlist_files_dir):
    os.makedirs(netlist_files_dir)

# read yosys template and replace the top module name
print(f"Synthesizing {len(verilog_files)} design(s) using Yosys...")
print("This may take a while... ⏳.")


for file in verilog_files:
    print(f"Synthesizing {file}...")

    file_name = file.split(os.path.sep)[-1].split('.')[0]
    with open(os.path.join(current_dir, 'yosys_script.template'), 'r') as file:
        output_file = file_name + '_synth.v'
        print(output_file)
        script = file.read().format(
            # input_file=file_name + ".v", liberty_file=sys.argv[1], top_module=file_name, output_file=os.path.join(netlist_files_dir, output_file))
            input_file=file_name + ".v", liberty_file=lib_file_path, output_file=os.path.join(netlist_files_dir, output_file))

    with open(os.path.join(verilog_files_dir, 'yosys_script.tcl'), 'w') as file:
        file.write(script)

    command = [
        'cmd', '/c', f'environment.bat & cd {verilog_files_dir} & yosys -s yosys_script.tcl']
    start = time.time()
    process = subprocess.Popen(command)

    while process.poll() is None:
        time.sleep(1)
        if time.time() - start > MAXTIMEOUT:
            process.kill()
            print("Yosys synthesis timed out. Moving to next design.. ❌")
            break

print("Yosys synthesis complete ✓.")
