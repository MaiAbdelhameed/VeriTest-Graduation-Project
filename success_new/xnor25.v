// tested
module xnor25 (
    input wire [2:0] a,
    input wire [2:0] b,
    output wire [2:0] out
);

assign out = ( { ~(a[2] ^ b[2]), ~(a[1] ^ b[1]), ~(a[0] ^ b[0])} );

endmodule
