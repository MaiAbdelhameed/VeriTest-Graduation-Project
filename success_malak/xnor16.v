module xnor16 (
    input wire a,
    input wire b,
    input wire c,
    input wire d,
    input wire e,
    output wire out
);

assign out = ~(a ^ b ^ c ^ d ^ e);

endmodule
