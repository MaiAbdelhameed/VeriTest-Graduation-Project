// tested
module sub4 (A,B,cin,sub,bo);

	input A,B,cin;
	output reg sub,bo;
	always @(*) begin 
		{bo,sub}=A-B-cin;
	end

endmodule