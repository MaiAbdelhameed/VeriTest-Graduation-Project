module xnor14 (
    input wire a,
    input wire b,
    input wire c,
    output wire out
);

assign out = ~(a ^ b ^ c);

endmodule