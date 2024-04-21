module adder2(A,B,cin,sum,cout);

	input A,B,cin;
	output sum,cout;
	assign sum = A ^ B ^ cin;
	assign cout = (A & B)|(cin & (A ^ B));

endmodule