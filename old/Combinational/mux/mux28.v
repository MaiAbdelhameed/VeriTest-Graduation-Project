module mux28 (input a, b, sel,
                    output y);

    assign y = (sel & b) | (~sel & a);
endmodule