module nand18 (
    input wire a,
    output wire out
);

assign out = (a & a) ? 1'b0 : 1'b1;

endmodule
