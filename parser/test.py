def slice_bits(input_str, start, end):
    # Convert negative indices to positive indices
    start_index = len(input_str) + start
    end_index = len(input_str) + end

    # Perform string slicing
    sliced_bits = input_str[start_index:end_index]

    return sliced_bits

# Example
input_bits = "01001"
start_index = 0
end_index = 2

result = slice_bits(input_bits, start_index, end_index)
print(result)
