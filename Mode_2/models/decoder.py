def compute(inputs):
    # in0 = inputs["in0"]

    # in1 = inputs["in1"]

    # input_string = in0 + in1

    input_string = inputs["in0"]

    output_string = "0000"

    decoder_index = int(input_string, 2)

    output_string = output_string[:decoder_index] + \
        '1' + output_string[decoder_index + 1:]

    out0 = output_string[0]
    out1 = output_string[1]
    out2 = output_string[2]
    out3 = output_string[3]

    return {'out0': out0, "out1": out1, "out2": out2, "out3": out3}


complement_str = ''.join(['1' if bit == '0' else '0' for bit in "1100"])
print(complement_str)
