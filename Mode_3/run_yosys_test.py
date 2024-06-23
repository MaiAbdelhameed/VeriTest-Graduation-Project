import os
import sys
import subprocess
import time
import signal


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

    verilog_file = sys.argv[1]
    verilog_files_dir = os.path.dirname(verilog_file)
    if not os.path.exists(verilog_file):
        # print("No verilog file found")
        return "failure"

    HOME = os.environ.get('VERITEST_HOME')
    lib_file_path = f'{HOME}/Mode_3/gate.lib'

    if not os.path.exists(lib_file_path):
        print("No liberty file found")
        return "failure"

    netlist_files_dir = os.path.dirname(verilog_file)

    if not os.path.exists(netlist_files_dir):
        os.makedirs(netlist_files_dir)

    # read yosys template and replace the top module name
    # print(f"Synthesizing design using Yosys...")

    file_name = verilog_file
    with open(f'{HOME}/Mode_3/yosys_script.template', 'r') as file:
        output_file = file_name[:-2] + '_synth.v'
        # print(output_file)
        script = file.read().format(
            # input_file=file_name + ".v", liberty_file=sys.argv[1], top_module=file_name, output_file=os.path.join(netlist_files_dir, output_file))
            input_file=file_name, liberty_file=lib_file_path, output_file=output_file)

    with open(os.path.join(verilog_files_dir, 'yosys_script.tcl'), 'w') as file:
        file.write(script)

    command = ["yosys", "-s", f"{verilog_files_dir}/yosys_script.tcl"]

    # Run the command
    subprocess.run(command, check=True)

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
