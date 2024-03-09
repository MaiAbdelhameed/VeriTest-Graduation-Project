
module mux14 (input [1:0] in,
                            input [1:0] sel,
                            output reg y);

    always @(*) begin
        case(sel)
            1'b0: y = in[0];
            1'b1: y = in[1];
        endcase
    end
    

endmodule