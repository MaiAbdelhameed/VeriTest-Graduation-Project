module mux3 (input a, b, sel,
                    output y);

    wire not_sel;

    assign not_sel = ~sel;
    assign y = (a & not_sel) | (b & sel);
endmodule