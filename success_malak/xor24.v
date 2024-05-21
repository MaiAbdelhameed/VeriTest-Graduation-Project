// tested
module xor24 (
    input wire [4:0] a,
    input wire [4:0] b,
    output wire [4:0] out
);

assign out = ( { (a[4] ^ b[4]),(a[3] ^ b[3]), (a[2] ^ b[2]), (a[1] ^ b[1]), (a[0] ^ b[0])} );

endmodule
