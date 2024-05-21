
// tested
module mux9 (input [1:0] a, b,
            input sel,
            output reg [1:0] y);

    always @(*) begin
        case(sel)
            0: y = a;
            1: y = b;
        endcase
    end
    
endmodule