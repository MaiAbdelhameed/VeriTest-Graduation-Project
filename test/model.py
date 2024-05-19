def compute(inputs):
    int1 = int(inputs[0], 2)
    int2 = int(inputs[1], 2)
    int3 = int(inputs[2], 2)

    result_int = int1 & int2 & int3

    # Convert the result back to binary string
    result_binary = str(bin(result_int)[2:])

    return {"OUT": result_binary}
