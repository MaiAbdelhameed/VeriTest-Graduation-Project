module ALU2(A,B,S,F);

	input [3:0] A,B;
	input [2:0] S;
	output reg [4:0] F;

	always @(*) begin
		case(S)
		0:F=0;
		1:F=B-A;
		2:F=A-B;
		3:F=A+B;
		4:F=A^B;
		5:F=A|B;
		6:F=A&B;
		7:F=5'b11111;
		endcase
	end

endmodule