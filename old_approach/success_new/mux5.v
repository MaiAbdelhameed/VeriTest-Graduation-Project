// tested using nand
module mux5 (input in0, input in1, input sel,
                    output out);

    assign out = ~(( ~((in1)&(sel)) ) & ( ~((in0)&(~(sel&sel))) ));

endmodule