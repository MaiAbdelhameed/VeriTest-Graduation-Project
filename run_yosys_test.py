import os
import sys
import subprocess
import time
import signal

MAXTIMEOUT = 30

def replace_not_in_file(file_path):
    # Open the file for reading and writing
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, file_path)
    with open(file_path, 'r+') as file:
        # Read the file content
        content = file.read()
        
        # Replace 'NOT' with 'not'
        updated_content = content.replace('NOT', 'not')
        
        # Move the file cursor to the beginning of the file
        file.seek(0)
        # Write the updated content to the file
        file.write(updated_content)
        # Truncate the file to the new length
        file.truncate()


def run_yosys():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir))
    yosys_suite_path = os.path.join(project_dir, 'oss-cad-suite')
    # print(yosys_suite_path)

    os.chdir(yosys_suite_path)

    verilog_files_dir = os.path.join(current_dir, './')

    verilog_file = os.path.join(current_dir, 'test_sample.v')
    if not os.path.exists(verilog_file):
        # print("No verilog file found")
        return "failure"


    

    lib_file_path = os.path.join(current_dir, 'gate.lib')

    if not os.path.exists(lib_file_path):
        print("No liberty file found")
        return "failure"
    
    netlist_files_dir = os.path.join(current_dir, './')

    if not os.path.exists(netlist_files_dir):
        os.makedirs(netlist_files_dir)

    # read yosys template and replace the top module name
    # print(f"Synthesizing design using Yosys...")


    file_name = verilog_file.split(os.path.sep)[-1].split('.')[0]
    with open(os.path.join(current_dir, 'yosys_script.template'), 'r') as file:
        output_file = file_name + '_synth.v'
        # print(output_file)
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
            # print("Yosys synthesis timed out. Moving to next design.. ❌")
            break

    # print("Yosys synthesis complete ✓.")
    replace_not_in_file(output_file)
    
    return "success"


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <verilog_file>")
    #     sys.exit(1)
    # verilog_file = sys.argv[1]
    result = run_yosys()
    # print(result)
    sys.exit(0 if result == "success" else 1)
