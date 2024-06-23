
def compute(specs_dict):
    input_size = 0
    output_size = 0
    # generate code
    output_code = ["def compute(inputs):"]

    # separate mode
    if (specs_dict["input_mode"] == "separate"):
        # read inputs lines
        for x in specs_dict["inputs"]:
            output_code.append(
                f'''\t{x['name']} = inputs["{x['name']}"]\n''')

        concatenation_line = f'''\tinput_string = '''
        for x in specs_dict["inputs"]:
            concatenation_line += f"{x['name']} + "
            # separate mode size calculation
            input_size += x['size']
        concatenation_line = concatenation_line[:-2]
        output_code.append(concatenation_line)

    # concatenated mode
    else:
        output_code.append(
            f"\tinput_string= inputs['{specs_dict['inputs'][0]['name']}']")
        # concatenation mode size calculation
        input_size += specs_dict['inputs'][0]['size']

    output_code.append('\toutput_string = "0000000"')
    output_code.append('\tinput_number = int(input_string, 2)')

    output_code.append('''\tif input_number == 0:
\t\toutput_string = "1111110"
\telif input_number == 1:
\t\toutput_string = "0110000"
\telif input_number == 2:
\t\toutput_string = "1101101"
\telif input_number == 3:
\t\toutput_string = "1111001"
\telif input_number == 4:
\t\toutput_string = "0110011"
\telif input_number == 5:
\t\toutput_string = "1011011"
\telif input_number == 6:
\t\toutput_string = "1011111"
\telif input_number == 7:
\t\toutput_string = "1110000"
\telif input_number == 8:
\t\toutput_string = "1111111"
\telif input_number == 9:
\t\toutput_string = "1111011"
\telif input_number == 10:
\t\toutput_string = "1110111"
\telif input_number == 11:
\t\toutput_string = "0011111"
\telif input_number == 12:
\t\toutput_string = "1001110"
\telif input_number == 13:
\t\toutput_string = "0111101"
\telif input_number == 14:
\t\toutput_string = "1001111"
\telif input_number == 15:
\t\toutput_string = "1000111"''')

    if (specs_dict["output_mode"] == "separate"):
        output_code.append('\toutput_string = output_string[::-1]')
        i = 0
        for x in specs_dict["output"]:
            output_size += x["size"]
            output_code.append(f'''\t{x['name']}=output_string[{i}]''')
            i += 1
    else:
        output_size += specs_dict['output'][0]['size']
        output_code.append(
            f'''\t{specs_dict['output'][0]['name']}=output_string''')

    return_line = "\treturn { "

    if (specs_dict["output_mode"] == "separate"):
        for x in specs_dict["output"]:
            return_line += (f'''"{x["name"]}": {x["name"]}, ''')
        return_line = return_line[:-2] + '}'
        output_code.append(return_line)
    else:
        return_line += f'''"{specs_dict['output'][0]['name']}": {specs_dict['output'][0]['name']} }}'''
        output_code.append(return_line)

    if not (output_size == 7 and input_size == 4):
        print(input_size)
        print(output_size)
        print("ERROR: Size mismatch for inputs and outputs")
        print("HINT:  number of outputs == 8 and number of inputs == 4")
        return ""

    return output_code
