module decoder12 (en,in,out);
	
	input [1:0] in;
    input en;
	output reg [3:0] out;
	
	always@(*) begin
	
	case(in)
		if(en) begin
		    0:out=4'b0001;
		    1:out=4'b0010;
		    2:out=4'b0100;
		    3:out=4'b1000;
        end
		else
		    out=4'b0000;
	
	endcase
	end

endmodule