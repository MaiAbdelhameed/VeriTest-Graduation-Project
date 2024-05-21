// tested using nand and not
module mux10 (input in0, in1, sel,
                    output out);

    assign out = ~(( ~((in1)&(sel)) ) & ( ~((in0)&(~sel)) ))

endmodule