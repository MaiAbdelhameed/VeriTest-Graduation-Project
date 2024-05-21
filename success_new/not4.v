module not4 (
    input wire a,
    output wire out
);

assign out = ~(a | a);

endmodule
