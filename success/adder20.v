module adder20
	(
	input wire A,
	input wire B,
	output reg sum,
	output reg carry_out
	);
	
	always@ (*) begin
		
		sum = A ^ B;
		carry_out = A & B;
	
	end

endmodule