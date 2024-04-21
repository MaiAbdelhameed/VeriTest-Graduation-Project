module sub1 ( a,b,c, sum, cout );

	input a,b,c;
	output sum, cout;
	
	assign sum = a ^ b ^ c;
	assign cout = ( b & ~a ) | (c & ( ~a | b ));
	
endmodule