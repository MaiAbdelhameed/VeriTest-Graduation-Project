// tested
module xor21 (
    input wire [1:0] a,
    input wire [1:0] b,
    output wire [1:0] out
);

assign out = ( {  (a[1] ^ b[1]), (a[0] ^ b[0])} );

endmodule
