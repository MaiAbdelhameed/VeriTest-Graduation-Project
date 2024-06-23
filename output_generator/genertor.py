import importlib
import sys
import os
import subprocess


Model_Name = ''


def read_starting_file(test_cases_filename):
    with open(test_cases_filename, 'r') as file:
        filename = file.readline().strip()
    try:
        print("IMPORTANT")
        print(filename)
        module = importlib.import_module(filename)
        print(f"Successfully imported module: {filename}")
        compute_function = getattr(module, 'compute', None)
        if compute_function is not None and callable(compute_function):
            global Model_Name
            Model_Name = filename
            return compute_function
        else:
            print("Module does not contain a 'compute' function or it is not callable.")

    except ModuleNotFoundError:
        print(f"Module {filename} not found or unable to import.")


def generate_output(test_cases_filename, compute):
    with open(test_cases_filename, 'r') as file:
        model_name = file.readline().strip()
        file.readline().strip()
        input = file.readline().strip()
        inputs_dict = {}
        input_names = []
        # loop to get all inputs
        while input != "#":
            key_start = input.find('(')
            key = input[:key_start]
            value = input[key_start + 1:-1]
            inputs_dict[key] = int(value)
            input_names.append(key)
            input = file.readline().strip()

        output = file.readline().strip()
        outputs_dict = {}
        output_names = []
        # loop to get all outputs
        while output != "#":
            key_start = output.find('(')
            key = output[:key_start]
            value = output[key_start + 1:-1]
            outputs_dict[key] = int(value)
            output_names.append(key)
            output = file.readline().strip()

        results_list = []

        input_value = file.readline().strip()
        while input_value != "EOF":
            if (input_value == "#"):
                input_value = file.readline().strip()
            test_case_dict = {}
            test_case_input = []
            for i in range(0, len(input_names)):
                test_case_dict[input_names[i]] = input_value
                test_case_input.append(input_value)
                input_value = file.readline().strip()
            result_item = {}

            result_item.update(test_case_dict)
            result_item.update(compute(test_case_dict))
            # result_item.update(compute(test_case_input))

            # print(test_case_dict)
            results_list.append(result_item)
    test_cases_file_content = ''

    # loop on all test cases and results and put them in a txt file to b read by the TestBench

    directory = 'results'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for test_case in results_list:
        for input_name in input_names:
            test_cases_file_content += test_case[input_name]

        for output_name in output_names:
            test_cases_file_content += test_case[output_name]
        test_cases_file_content += '\n'

    # Write the test cases to a file
    with open('./results/test_cases.txt', 'w') as file:
        file.write(test_cases_file_content)

    print("Test cases have been written to test_cases.txt file.")

    ###################################################

    # declaring input variables
    inputs_string = ''

    for input in input_names:
        inputs_string += f"reg [{inputs_dict[input]-1}:0]{input};\n"

    # declaring output variables
    outputs_string = ''
    for output in output_names:
        outputs_string += f"wire [{outputs_dict[output]-1}:0]{output};\n"
        outputs_string += f"reg [{outputs_dict[output]-1}:0]{output}_expected;\n"

    ####################################
    total_number_of_bits = sum(inputs_dict.values())+sum(outputs_dict.values())
    total_number_of_test_cases = len(results_list)
    data_variable = f"reg [0:{total_number_of_bits-1}] data [0:{total_number_of_test_cases-1}];"

    ####################################

    dut_instantiation_line = f"{Model_Name} dut(\n"

    for input in input_names:
        dut_instantiation_line += f".{input}({input}),\n"

    for output in output_names:
        dut_instantiation_line += f".{output}({output}),\n"

    dut_instantiation_line = dut_instantiation_line[:-2]

    dut_instantiation_line += "\n);"

    ###################################

    for_loop_line = f"for (i=0; i < {len(results_list)}; i=i+1) begin\n"

    ##########################

    variables_reading_from_array = '{'

    for i in range(0, len(input_names)):
        variables_reading_from_array += f"{input_names[i]},"
    for i in range(0, len(output_names)):
        variables_reading_from_array += f"{output_names[i]}_expected,"
    variables_reading_from_array = variables_reading_from_array[:-1]
    variables_reading_from_array += '}=data[i];'
    ###################################

    if_condition_line = "if ("

    for i in range(len(output_names)):
        if_condition_line += f'{output_names[i]}== {output_names[i]}_expected &&'

    if_condition_line = if_condition_line[:-2]

    if_condition_line += ')begin\n'
    ###################################

    failed_cases_display_line = '$display("INPUTS:\\n");\n'
    print("input names")
    print(input_names)
    for i in range(0, len(input_names)):
        failed_cases_display_line += f'$display("{input_names[i]} %b\\n",{input_names[i]});\n'
    failed_cases_display_line += '$display("OUTPUTS:\\n");\n'
    for i in range(0, len(output_names)):
        failed_cases_display_line += f'$display("{output_names[i]} %b ==> {output_names[i]}_expected %b \\n",{output_names[i]},{output_names[i]}_expected);\n'

    ###################################
    # Writing VeriLog code
    with open('./results/generated_tb.v', 'w') as file:
        file.write("""`timescale 1ns/1ns
module tb ();\n""")
        # writing input strings
        file.write(inputs_string)
        file.write("\n\n")
        # writing output strings
        file.write(outputs_string)
        file.write("\n\n")
        # writing data variable
        file.write(data_variable)
        file.write("\n\n")
        # reading from input file
        file.write('initial $readmemb("test_cases.txt", data);')
        file.write("\n\n")
        # defining variables
        file.write("""integer i;
integer total_cases;
integer successful_cases;
integer failed_cases;
""")
        file.write("\n\n")
        file.write(dut_instantiation_line)
        file.write("\n\n")
        file.write('''initial begin



    // setting the counters
    total_cases=0;
    successful_cases=0;
    failed_cases=0;
''')
        # for loop line
        file.write(for_loop_line)

        file.write(
            f"total_cases= total_cases+1;\n{variables_reading_from_array}\n#5\n")
        file.write(if_condition_line)

        file.write("""$display("test case %d==> Success",total_cases);
$display("#####################################################");
successful_cases=successful_cases+1;\n""")
        file.write("""end \n else begin
$display("test case %d==> Fail",total_cases);\n""")
        file.write(failed_cases_display_line)
        file.write(
            """$display("#####################################################");\n""")
        file.write("""failed_cases=failed_cases+1;\n""")
        file.write(
            f"\nend\nend\n")
        file.write("""$display("Summary:\\n total cases==>%d \\n successful cases==>%d \\n failed cases==>%d",total_cases,successful_cases,failed_cases);\n """)
        file.write("end\nendmodule")


# Check if arguments are provided
if len(sys.argv) > 1:

    test_case_file = sys.argv[1:][0]

    print("Command-line arguments:", test_case_file)
else:
    print("No command-line arguments provided please provide test cases filename")
    sys.exit(1)

compute = read_starting_file(test_case_file)
generate_output(test_case_file, compute)

# compile testBench and run simulation

# Specify the path to your Bash script
current_directory = os.path.dirname(os.path.abspath(__file__))
bash_script_path = current_directory+'/run_simulation.sh'
print(current_directory+f"/{Model_Name}.v")
try:
    subprocess.run(['bash', bash_script_path,
                   current_directory+f"/{Model_Name}.v"], check=True)
    # print("Bash script executed successfully")
except subprocess.CalledProcessError as e:
    print("Error executing Bash script:", e)
