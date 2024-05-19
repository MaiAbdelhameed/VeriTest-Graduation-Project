
def compute(specs_dict):

    circuit_type = specs_dict["type"]
    # output_file_text
    output_code = []
    # get operation symbol
    operation_symbol = ''
    if (circuit_type in ['and', 'nand']):
        operation_symbol = '&'
    elif (circuit_type in ['or', 'nor']):
        operation_symbol = '|'
    elif (circuit_type in ['xor', 'xnor']):
        operation_symbol = '^'
    # get number of inputs
    number_of_inputs = int(len(specs_dict['inputs']))

    input_names = specs_dict["inputs"]
    output_name = specs_dict['output']

    result_line = '\tresult_int = '
    output_code.append('def compute(inputs):')

    if ("operation_type" in specs_dict and specs_dict["operation_type"] == "bitwise"):
        # bitwise operation code
        # inputs initialization
        for i in range(0, number_of_inputs):
            output_code.append(
                f'''\t{input_names[i]['name']} = inputs["{input_names[i]['name']}"]\n''')

        output_code.append(f"""\tresult_binary='' """)

        # bitwise calculation loop
        output_code.append(
            f"""\tfor i in range (0,{input_names[0]["size"]}):""")

        result_calculation_line = '\t\tresult_binary += str(bin('
        for input in input_names:

            result_calculation_line += f""" int({input["name"]}[i]) &"""
        result_calculation_line = result_calculation_line[:-2]
        result_calculation_line += '))[2:]'
        output_code.append(result_calculation_line)

        # optional bitwise code
        if circuit_type in ['nand', 'nor', 'xnor']:
            output_code.append("\tbitmask = (1 << len(result_binary)) - 1")
            output_code.append("\tbitwise_not = int(result_binary) ^ bitmask")
            output_code.append(
                "\tresult_binary = format(bitwise_not, 'b').zfill(len(result_binary))")
        # output return line
        output_code.append(
            f'\treturn{{ \'{output_name}\' : result_binary }} \n')
    else:
        # logical operation code

        # inputs initialization and result calculation line generation
        for i in range(0, number_of_inputs):

            output_code.append(
                f'''\t{input_names[i]['name']} = int(inputs["{input_names[i]['name']}"],2)\n''')
            result_line += f'{input_names[i]["name"]} {operation_symbol} '
        result_line = result_line[:-2]+"\n"
        output_code.append(result_line)
        if circuit_type in ['nand', 'nor', 'xnor']:
            output_code.append('\tresult_int = not result_int')
        output_code.append('\tresult_binary = str(bin(result_int)[2:])')

        output_code.append(
            f'\treturn{{ \'{output_name}\' : result_binary }} \n')

    return output_code
