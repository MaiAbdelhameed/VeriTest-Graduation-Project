// tested
module xnor27 (
    input wire [7:0] a,
    input wire [7:0] b,
    output wire [7:0] out
);

assign out = ( { ~(a[7] ^ b[7]),~(a[6] ^ b[6]), ~(a[5] ^ b[5]), ~(a[4] ^ b[4]), ~(a[3] ^ b[3]),
                    ~(a[2] ^ b[2]), ~(a[1] ^ b[1]), ~(a[0] ^ b[0])} );

endmodule
