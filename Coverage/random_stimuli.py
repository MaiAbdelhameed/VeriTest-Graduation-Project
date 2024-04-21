import random
import sys
sys.path.append("..")
from PARSER.preprocessing.find import get_input_output




def generate_binary_string(n):
    binary_string = str(n) + "'b"
    # Loop to generate binary string of length n
    for i in range(n):
        # randint function to generate 0, 1 randomly and convert the result to str
        temp = str(random.randint(0, 1))

        # Concatenate the random 0, 1 to the binary_string
        binary_string += temp
    return(binary_string)

def input_output_wire(module_name):
    input_output_wire2, _ = get_input_output(module_name)
    input_output_wire = input_output_wire2.copy()
    for key, value in input_output_wire[0].items():
        input_output_wire[0][key] = int(value["msb"]) - int(value["lsb"]) + 1
    
    for key, value in input_output_wire[1].items():
        input_output_wire[1][key] = int(value["msb"]) - int(value["lsb"]) + 1

    for key, value in input_output_wire[2].items():
        input_output_wire[2][key] = int(value["msb"]) - int(value["lsb"]) + 1

    return input_output_wire

def output_file(in_out,test_cases):

    output_file = "output/output_file.txt"

    # Open the file in write mode ('w')
    with open(output_file, 'w') as file:
        name = "my_module"
        file.write(name+'\n')
        file.write("#\n")
        # Write data for inputs
        for key, value in in_out[0].items(): # in_out[0] is a dictionary for the inputs
            # Write key-value pairs to the file
            file.write(f"{key}({value})\n")
        file.write("#\n")
        # Write data for outputs
        for key, value in in_out[1].items(): # in_out[1] is a dictionary for the outputs
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

        file.write("EOF") # End of file



def random_stimuli(n, module_name):
    # Testcases Dictionary
    input_to_testcases_dict = dict()

    # Get input sizes
    sizes = input_output_wire(module_name)
    print(sizes)
    #print(sizes[0])
    input_sizes_dict = sizes[0]
    
    
    for key,_ in input_sizes_dict.items():
        # List of testcases
        testcases = list()
        input_to_testcases_dict.update({key:testcases})

    for _ in range(n):
        # Loop on all inputs and call generate_binary_string with input size to generate random testcases for each
        for key,value in input_to_testcases_dict.items():
            input_testcase = generate_binary_string(input_sizes_dict[key])
            value.append(input_testcase)
            #print(f"The value for key '{key}' is '{input_testcase}'")
    print("here", input_to_testcases_dict)
    while(1):
        pass
    # output_file(sizes,input_to_testcases_dict)
    # return input_to_testcases_dict


# random_stimuli(3, "PARSER/files/my_module.v")