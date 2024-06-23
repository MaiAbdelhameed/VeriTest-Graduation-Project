def compute(inputs):
	a = inputs["a"]

	b = inputs["b"]

	result_binary='' 
	for i in range (0,1):
		result_binary += str(bin( int(a[i]) & int(b[i])))[2:]
	return{ 'out' : result_binary } 

