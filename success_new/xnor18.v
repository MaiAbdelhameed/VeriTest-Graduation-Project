module xnor18 (
    input wire a,
    input wire b,
    input wire c,
    input wire d,
    input wire e,
    input wire f,
    input wire g,
    output wire out
);

assign out = ~(a ^ b ^ c ^ d ^ e ^ f ^ g);

endmodule
