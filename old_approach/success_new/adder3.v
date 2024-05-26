// tested
module adder3(A,B,cin,sum,cout);

	input A,B,cin;
	output sum,cout;

	reg sum_temp,cout_temp;

	assign sum = sum_temp;
	assign cout = cout_temp;
	always @(*) begin
		{cout_temp,sum_temp}=A+B+cin;
	
	end

endmodule