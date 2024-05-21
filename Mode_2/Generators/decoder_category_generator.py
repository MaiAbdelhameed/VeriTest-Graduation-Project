
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

    output_size = 0

    if (specs_dict["output_mode"] == "separate"):

        for x in specs_dict["output"]:
            output_size += x["size"]

    else:
        # concatenation mode size calculation
        output_size = specs_dict["output"][0]["size"]

    output_code.append(f'''\toutput_string="{"0"*output_size}"''')

    output_code.append(f'''\tdecoder_index = int(input_string, 2)''')
    output_code.append(
        f'''\toutput_string = output_string[:decoder_index] + '1' + output_string[decoder_index + 1:]''')

    if (specs_dict["output_mode"] == "separate"):
        i = 0
        for x in specs_dict["output"]:
            output_code.append(f'''\t{x['name']}=output_string[{i}]''')
            i += 1
    else:
        output_code.append(
            f'''\t{specs_dict['output'][0]['name']}=output_string''')

    return_line = "\treturn { "

    if (specs_dict["output_mode"] == "separate"):
        output_code.append(' output_string = output_string[::-1]')
        for x in specs_dict["output"]:
            return_line += (f'''"{x["name"]}": {x["name"]}, ''')
        return_line = return_line[:-2] + '}'
        output_code.append(return_line)
    else:
        return_line += f'''"{specs_dict['output'][0]['name']}": {specs_dict['output'][0]['name']} }}'''
        output_code.append(return_line)

    if (pow(2, input_size) != output_size):
        print(input_size)
        print(output_size)
        print("ERROR: Size mismatch for inputs and outputs")
        print("HINT: pow(2,number of inputs) == number of outputs")

    return output_code
