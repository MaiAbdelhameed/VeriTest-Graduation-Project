
module mux9 (input a, b,
            input sel,
            output reg y);

    always @(*) begin
        case(sel)
            0: y = a;
            1: y = b;
        endcase
    end
    
endmodule