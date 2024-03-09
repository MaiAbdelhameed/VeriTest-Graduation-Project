module sub5 (A,B,cin,sub,bo);

	input A,B,cin;
	output sub,bo;

	assign sub = A^B^cin;
	assign bo = (~A&B)|(~A&cin)|(B&cin);

endmodule