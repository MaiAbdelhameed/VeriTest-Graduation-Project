module comparator8 (
    input [3:0] a,
    input [3:0] b,
    output reg eq,
    output reg greater,
    output reg less
);

    always @(*) begin
        case ({a > b, a == b, a < b})
            3'b100: begin
	            eq = 1; greater = 0; less = 0; // Equal
	        end
          
            3'b010: begin 
	            eq = 0; greater = 1; less = 0; // Greater
	        end

            3'b001: begin
	            eq = 0; greater = 0; less = 1; // Less
	        end
            default: begin
                eq = 0; greater = 0; less = 0; // Handle unknown cases
            end
        endcase
    end

endmodule