def compute(inputs):
    # selectors

    # separate
    # s = [inputs["s0"], inputs["s1"]]
    # s.reverse()
    ###############
    # concatenated
    s = inputs["s"]

    # common
    s = [int(char) for char in s]

    selector_decimal_number = 0
    for bit in s:
        selector_decimal_number = (selector_decimal_number << 1) | bit

    #################################################################

    # inputs

    # separate
    # input_numbers = [inputs["in0"], inputs["in1"],
    #                  inputs["in2"], inputs["in3"]]

    # concatenated

    input_numbers = inputs["in"]

    return ({"out": input_numbers[selector_decimal_number]})


print(compute({"s": "10", "in": "1101"}))
