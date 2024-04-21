module adder4(A,B,cin,sum,cout);

	input A,B,cin;
	output sum,cout;

	wire out1,out2,out3,out4,out6,out7;

	and a1(out1,A,B);
	and a2(out2,A,cin);
	and a3(out3,B,cin);

	or a4(out4,out1,out2);
	or a5(cout,out4,out3);

	xor a6(out6,A,B);
	xor a7(sum,out6,cin);

endmodule