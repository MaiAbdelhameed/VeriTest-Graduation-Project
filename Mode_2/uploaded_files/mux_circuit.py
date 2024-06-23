def compute(inputs):
    s = inputs["s"]
    s = [int(char) for char in s]
    selector_decimal_number = 0
    for bit in s:
        selector_decimal_number = (selector_decimal_number << 1) | bit
    input_numbers = inputs["in"]
    return ({"out": input_numbers[selector_decimal_number]})
