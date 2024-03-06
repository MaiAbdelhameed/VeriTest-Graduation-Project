module mux33 (input a, b, sel,
                   output reg y);

    // Multiplexer logic using case statement
    always @(*) begin
        case(sel)
            1'b0: y = a;
            1'b1: y = b;
        endcase
    end
endmodule