def compute(specs_dict):

    category = specs_dict['type']

    # generate output code
    output_code = ['def compute(inputs):']

    number_of_inputs = int(len(specs_dict['inputs']))
    input_names = specs_dict['inputs']
    for i in range(0, number_of_inputs):
        output_code.append(
            f'''\t{input_names[i]['name']} = inputs["{input_names[i]['name']}"]\n''')

    # flags code
    output_code.append("""\tsign_flag = '0'
\tzero_flag = '0'
\todd_parity_flag = '0'
\teven_parity_flag = '0'
\todd_flag = '0'
\teven_flag = '0'
\tcarry_out= '0'
\toverflow_flag = '0'""")

    # carry in code

    if ("carry_in" in specs_dict):
        output_code.append(
            f"""\tcarry_in = int(inputs["{specs_dict["carry_in"]["name"]}"])""")
    else:
        output_code.append("\tcarry_in=0")

    result_line = "\tresult_binary = "
    if ("mode" in specs_dict and specs_dict["mode"] == "signed"):
        for x in input_names:
            name = x["name"]
            result_line += f"int({name}[1:], 2) * (1 - 2 * int({name}[0])) + "
        result_line = result_line[:-2]
    else:
        for x in input_names:
            name = x["name"]
            result_line += f"int({name}, 2) + "
        result_line = result_line[:-2]
    output_code.append(result_line)

    # flag calculation

    output_code.append(f"""\tresult_binary += carry_in
\tsign_flag = '1' if result_binary < 0 else '0'
\tzero_flag = '1' if result_binary == 0 else '0'
\todd_flag = '1' if result_binary % 2 != 0 else '0'
\teven_flag = '1' if result_binary % 2 == 0 else '0'

\tbinary_form = f'''{{abs(result_binary):0{specs_dict["output"]["size"]}b}}'''

\tif (result_binary < 0):
\t\tbinary_form = '1' + binary_form[1:]
\tresult_binary = binary_form
\tone_count = result_binary.count('1')
\tif (one_count % 2 == 0):
\t\teven_parity_flag = '1'
\t\todd_parity_flag = '0'
\telse:
\t\teven_parity_flag = '0'
\t\todd_parity_flag = '1'

""")

    # overflow flag and carry flag
    output_code.append(f"""\tif (len(result_binary) > {specs_dict["output"]["size"]}):
\t\tcarry_out = '1'
\t\toverflow_flag = '1'
\t\tresult_binary = result_binary[1:]
""")

    # return line
    return_line = "\treturn { "

    return_line += f"""'{specs_dict["output"]["name"]}':result_binary,"""

    if ("sign_flag" in specs_dict):
        return_line += f"""'{specs_dict["sign_flag"]['name']}':sign_flag,"""
    if ("zero_flag" in specs_dict):
        return_line += f"""'{specs_dict["zero_flag"]['name']}':zero_flag,"""
    if ("odd_parity_flag" in specs_dict):
        return_line += f"""'{specs_dict["odd_parity_flag"]['name']}':odd_parity_flag,"""
    if ("even_parity_flag" in specs_dict):
        return_line += f"""'{specs_dict["even_parity_flag"]['name']}':even_parity_flag,"""
    if ("odd_flag" in specs_dict):
        return_line += f"""'{specs_dict["odd_flag"]['name']}':odd_flag,"""
    if ("even_flag" in specs_dict):
        return_line += f"""'{specs_dict["even_flag"]['name']}':even_flag,"""
    if ("overflow_flag" in specs_dict):
        return_line += f"""'{specs_dict["overflow_flag"]['name']}':overflow_flag,"""
    if ("carry_out" in specs_dict):
        return_line += f"""'{specs_dict["carry_out"]['name']}':carry_out,"""

    return_line = return_line[:-1] + '}'
    output_code.append(return_line)

    # check input and output size eligibility
    output_expected_bits = max(
        specs_dict["inputs"][0]["size"], specs_dict["inputs"][1]["size"])+1

    if (len(specs_dict["inputs"]) > 2):
        for i in range(2, len(specs_dict["inputs"])):
            output_expected_bits = max(
                output_expected_bits, specs_dict["inputs"][1]["size"])+1

    if not ((output_expected_bits == specs_dict["output"]["size"] or output_expected_bits - 1 == specs_dict["output"]["size"])):

        print("ERROR => output variable size is too small")
        print(f'EXPECTED {output_expected_bits} or {output_expected_bits-1}')
        return ("")

    return output_code
