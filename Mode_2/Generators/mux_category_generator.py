
def compute(specs_dict):
    selector_size = 0
    input_size = 0
    # generate code
    output_code = ["def compute(inputs):"]

    # separate mode
    if (specs_dict["selector_mode"] == "separate"):
        # read inputs lines
        selector_size = len(specs_dict["selectors"])
        selector_line = "\ts=["
        for x in specs_dict["selectors"]:
            selector_line += f'inputs["{x["name"]}"],'
        selector_line = selector_line[:-1]
        selector_line += "]"
        output_code.append(selector_line)
        output_code.append("\ts.reverse()")
    # concatenated mode
    else:
        output_code.append(
            f'\ts=inputs["{specs_dict["selectors"][0]["name"]}"]')
    ############################
    output_code.append("\ts = [int(char) for char in s]")
    output_code.append('''\tselector_decimal_number = 0
\tfor bit in s:
\t\tselector_decimal_number = (selector_decimal_number << 1) | bit''')

    ############################
    # separate mode
    if (specs_dict["input_mode"] == "separate"):
        input_size = len(specs_dict["inputs"])
        input_numbers_line = "\tinput_numbers=["
        for x in specs_dict["inputs"]:
            input_numbers_line += f'inputs["{x["name"]}"],'
        input_numbers_line = input_numbers_line[:-1]
        input_numbers_line += "]"
        output_code.append(input_numbers_line)
    # concatenated mode
    else:
        output_code.append(
            f'\tinput_numbers=inputs["{specs_dict["inputs"][0]["name"]}"]')

    return_line = f'\treturn ({{"{specs_dict["output"]["name"]}": input_numbers[selector_decimal_number]}})'
    output_code.append(return_line)
    if not (selector_size ** 2 == input_size):
        print("selector and input size mismatch")
        print("selector_size^2 == input_size")
        return ""

    return output_code
