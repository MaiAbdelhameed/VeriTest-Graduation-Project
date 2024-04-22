module xor23 (
    input wire [3:0] a,
    output wire out
);

assign out = (^a == 1'b1) ? 1'b1 : 1'b0;

endmodule
