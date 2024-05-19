def compute(inputs):
    in1 = inputs["in1"]

    in2 = inputs["in2"]

    in3 = inputs["in3"]

    # flags
    sign_flag = '0'
    zero_flag = '0'
    odd_parity_flag = '0'
    even_parity_flag = '0'
    odd_flag = '0'
    even_flag = '0'
    carry_out = '0'
    overflow_flag = '0'
    carry_in = '0'
    # carry_in = int(inputs["carry_in"])
    # signed
    # result_binary = int(in1[1:], 2) * (1 - 2 * int(in1[0])) + int(in2[1:], 2) * (
    #     1 - 2 * int(in2[0])) + int(in3[1:], 2) * (1 - 2 * int(in3[0]))

    # unsigned
    result_binary = int(in1, 2) + int(in2, 2) + int(in3, 2)

    result_binary += int(carry_in, 2)
    sign_flag = '1' if result_binary < 0 else '0'
    zero_flag = '1' if result_binary == 0 else '0'
    odd_flag = '1' if result_binary % 2 != 0 else '0'
    even_flag = '1' if result_binary % 2 == 0 else '0'

    binary_form = f"{abs(result_binary):0{4}b}"

    if (result_binary < 0):
        binary_form = '1' + binary_form[1:]
    result_binary = binary_form

    one_count = result_binary.count('1')

    if (one_count % 2 == 0):
        even_parity_flag = '1'
        odd_parity_flag = '0'
    else:
        even_parity_flag = '0'
        odd_parity_flag = '1'

    if (len(result_binary) > 4):

        carry_out = 1
        overflow_flag = 1
        result_binary = result_binary[1:]

    # print([
    #     sign_flag,
    #     zero_flag,
    #     odd_parity_flag,
    #     even_parity_flag,
    #     odd_flag,
    #     even_flag,
    # ])
    return {'out': result_binary, "carry_out": carry_out, "overflow_flag": overflow_flag}


print(compute({"in1": "111", "in2": "11", "in3": "110"}))
# binary_string = '000000011'
# result = int(binary_string[1:], 2) * (1 - 2 * int(binary_string[0]))
# print(result)
# n = 1  # Number of bits
# number = -2  # Example signed integer

# binary_form = f"{abs(number):0{n}b}"

# if (number < 0):
#     binary_form = '1' + binary_form[1:]


# print(binary_form)


"""
1111101

111
001


1101

110
"""
