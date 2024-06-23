import os
import re
from PARSER.GraphAPI import GraphAPI
from PARSER.preprocessing.find import get_input_output
import random
import sys
sys.path.append("..")


def generate_binary_string(n):
    binary_string = str(n) + "'b"
    # Loop to generate binary string of length n
    for i in range(n):
        # randint function to generate 0, 1 randomly and convert the result to str
        temp = str(random.randint(0, 1))

        # Concatenate the random 0, 1 to the binary_string
        binary_string += temp
    return (binary_string)


def input_output_wire(PATH):
    input_output_wire2, _ = get_input_output(PATH)
    input_output_wire = input_output_wire2.copy()
    for key, value in input_output_wire[0].items():
        input_output_wire[0][key] = int(value["msb"]) - int(value["lsb"]) + 1

    for key, value in input_output_wire[1].items():
        input_output_wire[1][key] = int(value["msb"]) - int(value["lsb"]) + 1

    for key, value in input_output_wire[2].items():
        input_output_wire[2][key] = int(value["msb"]) - int(value["lsb"]) + 1

    return input_output_wire


def output_file(in_out, test_cases, path):
    HOME = os.environ.get('VERITEST_HOME')
    output_file = f"{HOME}/output/output_file.txt"

    # Open the file in write mode ('w')
    with open(output_file, 'w') as file:
        name = path[:-2]
        file.write(name+'\n')
        file.write("#\n")
        # Write data for inputs
        # in_out[0] is a dictionary for the inputs
        for key, value in in_out[0].items():
            # Write key-value pairs to the file
            file.write(f"{key}({value})\n")
        file.write("#\n")
        # Write data for outputs
        # in_out[1] is a dictionary for the outputs
        for key, value in in_out[1].items():
            # Write key-value pairs to the file
            file.write(f"{key}({value})\n")

        # Get the values from test_cases dictionary
        values = list(test_cases.values())

        # Iterate over the zipped lists (parallel iterations)
        for items in zip(*values):
            # Write each item to the file
            file.write("#\n")
            for item in items:
                file.write(item[3:] + "\n")

        file.write("EOF")  # End of file


def random_stimuli(n, PATH):
    # Testcases Dictionary
    input_to_testcases_dict = dict()

    # Get input sizes
    sizes = input_output_wire(PATH)
    # print(sizes)
    # print(sizes[0])
    input_sizes_dict = sizes[0]

    for key, _ in input_sizes_dict.items():
        # List of testcases
        testcases = list()
        input_to_testcases_dict.update({key: testcases})

    for _ in range(n):
        # Loop on all inputs and call generate_binary_string with input size to generate random testcases for each
        for key, value in input_to_testcases_dict.items():
            input_testcase = generate_binary_string(input_sizes_dict[key])
            value.append(input_testcase)
            # print(f"The value for key '{key}' is '{input_testcase}'")

    print(input_to_testcases_dict)
    # output_file(sizes,input_to_testcases_dict)
    return input_to_testcases_dict, sizes


def Insert_Random_Input(input_test_cases, input_dict, dict_of_new_inputs, CODE_GRAPH):
    for key, value in input_test_cases.items():
        if key not in input_dict:
            continue
        size = input_dict[key]
        vec = generate_binary_string(size)
        value.append(vec)

    for key, value in dict_of_new_inputs.items():

        if "[" in key:
            if ":" in key:
                RANGE = re.match(r".*(\[\d+:\d+\])", key).group(1)
                name_of_var = key.split("[")[0]
                x = key[2:-1]
                end, start = x.split(":")
                new_val = None
                Range_len = abs(int(end) - int(start)) + 1
                if len(value) < Range_len:
                    new_val = "0" * (abs(Range_len - len(value))) + value
                else:
                    new_val = value

                vec = input_test_cases[name_of_var][-1]
                vec = re.sub("\d+'b", "", vec)
                vec = vec[::-1]
                vec = [X for X in vec]
                vec[int(start):int(end)+1] = new_val
                # ["0", "1", "0"]
                vec = "".join(vec)
                size = str(input_dict[name_of_var])

                input_test_cases[name_of_var][-1] = size + "'b" + vec[::-1]

            else:
                index = re.match(r".*\[(\d+)\]", key).group(1)
                name_of_var = re.match(r"(.*)\[\d+\]", key).group(1)
                x = input_test_cases[name_of_var][-1]
                prefix = re.match("(\d+'b).*", x).group(1)
                x = re.sub("\d+'b", "", x)
                x_list = [M for M in x]
                m = x_list[::-1]
                m[int(index)] = value
                m = m[::-1]
                new_str = "".join(m)
                input_test_cases[name_of_var][-1] = prefix + new_str
        else:
            new_val = None
            size = input_dict[key]
            if len(value) < size:
                new_val = "0" * (abs(size - len(value))) + value
                prefix = str(size) + "'b"
                input_test_cases[key][-1] = prefix + new_val
            else:
                prefix = str(size) + "'b"
                new_val = prefix + value
                input_test_cases[key][-1] = new_val

    dict_of_new_test_cases = dict()
    for key, value in input_test_cases.items():
        if key in input_dict:
            val = input_test_cases[key][-1]
            dict_of_new_test_cases.update({key: [val]})

    API = GraphAPI(CODE_GRAPH)
    outputs = API.calc_output(dict_of_new_test_cases)

    for key, value in outputs.items():
        input_test_cases[key].extend(value)
