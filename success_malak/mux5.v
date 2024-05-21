// tested using nand
module mux5 (input in0, in1, sel,
                    output out);

    assign out = ~(( ~((in1)&(sel)) ) & ( ~((in0)&(~(sel&sel))) ))

endmodule