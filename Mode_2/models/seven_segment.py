def compute(inputs):
    # in0 = inputs["in0"]

    # in1 = inputs["in1"]

    # in2 = inputs["in2"]

    # in3 = inputs["in3"]

    # input_string = in0 + in1 + in2 + in3

    input_string = inputs["in0"]

    output_string = "0000000"

    input_number = int(input_string, 2)

    if input_number == 0:
        output_string = "1111110"
    elif input_number == 1:
        output_string = "0110000"
    elif input_number == 2:
        output_string = "1101101"
    elif input_number == 3:
        output_string = "1111001"
    elif input_number == 4:
        output_string = "0110011"
    elif input_number == 5:
        output_string = "1011011"
    elif input_number == 6:
        output_string = "1011111"
    elif input_number == 7:
        output_string = "1110000"
    elif input_number == 8:
        output_string = "1111111"
    elif input_number == 9:
        output_string = "1110011"
    elif input_number == 10:
        output_string = "1110111"
    elif input_number == 11:
        output_string = "0011111"
    elif input_number == 12:
        output_string = "1001110"
    elif input_number == 13:
        output_string = "0111101"
    elif input_number == 14:
        output_string = "1001111"
    elif input_number == 15:
        output_string = "1000111"

    out0 = output_string[0]
    out1 = output_string[1]
    out2 = output_string[2]
    out3 = output_string[3]

    return {'out0': out0, "out1": out1, "out2": out2, "out3": out3}


complement_str = ''.join(['1' if bit == '0' else '0' for bit in "1100"])
print(complement_str)
