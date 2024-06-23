def compute(inputs):
	input_string= inputs['in']
	output_string="0000"
	decoder_index = int(input_string, 2)
	output_string = output_string[:decoder_index] + '1' + output_string[decoder_index + 1:]
	output_string = output_string[::-1]
	out=output_string
	return { "out": out }
