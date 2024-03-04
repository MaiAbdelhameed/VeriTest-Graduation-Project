module decoder1 (in,out);
	
	input [1:0] in;
	output reg [3:0] out;
	
	always@(*) begin
	
	case(in)
		
		0:out=4'b1000;
		1:out=4'b0100;
		2:out=4'b0010;
		3:out=4'b0001;
		
		default:out=4'b0000;
	
	endcase
	end

endmodule