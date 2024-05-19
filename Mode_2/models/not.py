def compute(inputs):
    in1 = inputs["in1"]

    in2 = inputs["in2"]

    in3 = inputs["in3"]

    out1 = ''.join(['1' if bit == '0' else '0' for bit in in1])
    out2 = ''.join(['1' if bit == '0' else '0' for bit in in2])
    out3 = ''.join(['1' if bit == '0' else '0' for bit in in3])
    return {'out1': out1, "out2": out2, "out3": out3}


complement_str = ''.join(['1' if bit == '0' else '0' for bit in "1100"])
print(complement_str)
