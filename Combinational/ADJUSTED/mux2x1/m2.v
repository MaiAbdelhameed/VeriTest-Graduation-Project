module mux_dataflow(input a, b, sel,
                    output y);

    assign y = (sel & b) | (~sel & a);
endmodule