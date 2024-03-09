module xor15 (
    input wire a,
    input wire b,
    output wire out
);

assign out = (a ^ b == 1'b1) ? 1'b1 : 1'b0;

endmodule
