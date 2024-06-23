def compute(inputs):
    # in0 = inputs["in0"]

    # in1 = inputs["in1"]

    # input_string = in0 + in1

    input_string = inputs["in0"]

    output_num = input_string.find('1')

    output_string = f"{abs(output_num):0{2}b}"
    # output_string = output_string[::-1]
    out0 = output_string[0]
    out1 = output_string[1]

    # out0 = output_string

    return {'out0': out0, "out1": out1}


print(compute({"in0": "0001"}))
