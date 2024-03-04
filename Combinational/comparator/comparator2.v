module comparator2 (A,C,out);

	input [3:0]A;
	input [3:0]C;
	output reg[1:0]out;

	always@(*) begin

	if(A>C)
		out=2'b00;
	else if(A<C)
		out=2'b01;
	else
		out=2'b10;
	end

endmodule