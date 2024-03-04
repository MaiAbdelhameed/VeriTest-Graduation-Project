module mux33 (input a, b, sel,
                   output y);

    // Multiplexer logic using case statement
    case(sel)
        1'b0: y = a;
        1'b1: y = b;
    endcase

endmodule
