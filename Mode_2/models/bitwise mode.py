def compute(inputs):
    in1 = inputs["in1"]

    in2 = inputs["in2"]

    in3 = inputs["in3"]

    result_binary = ''
    for i in range(0, 2):
        result_binary += str(bin(int(in1[i]) & int(in2[i]) & int(in3[i])))[2:]

    bitmask = (1 << len(result_binary)) - 1

    bitwise_not = int(result_binary) ^ bitmask

    result_binary = format(bitwise_not, 'b').zfill(len(result_binary))
    return {'out': result_binary}


print(compute({"in1": "11", "in2": "10", "in3": "01"}))
