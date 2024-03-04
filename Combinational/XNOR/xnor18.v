module xnor18 (
    input wire a,
    output wire out
);

assign out = ~(a ^ a);

endmodule
