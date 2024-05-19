def compute(specs_dict):

    # generate code
    output_code = ["def compute(inputs):"]

    # read inputs lines
    for x in specs_dict["inputs_outputs"]:
        output_code.append(
            f'''\t{x['input_name']} = inputs["{x['input_name']}"]\n''')

    # calculate outputs lines
    for x in specs_dict["inputs_outputs"]:
        output_code.append(
            f'''\t{x['output_name']} = ''.join(['1' if bit == '0' else '0' for bit in {x["output_name"]}])''')

    return_line = '\treturn { '
    # return_line
    for x in specs_dict["inputs_outputs"]:
        return_line += f"""'{x["output_name"]}': {x["output_name"]},"""
    return_line = return_line[:-1] + "}"
    output_code .append(return_line)

    return output_code
