// tested
module xnor28 (
    input wire [4:0] a,
    input wire [4:0] b,
    output reg [4:0] out
);

always @(*) begin

    out[4] = ~(a[4] ^ b[4]);

    out[3] = ~(a[3] ^ b[3]);
    out[2] = ~(a[2] ^ b[2]);
    out[1] = ~(a[1] ^ b[1]);
    out[0] = ~(a[0] ^ b[0]);

end


endmodule