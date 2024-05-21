// tested
module nand13 (
    input wire [7:0] a,
    input wire [7:0] b,
    output reg [7:0] out
);

always @(*) begin
    out[7] = ~(a[7] & b[7]);
    out[6] = ~(a[6] & b[6]);
    out[5] = ~(a[5] & b[5]);
    out[4] = ~(a[4] & b[4]);

    out[3] = ~(a[3] & b[3]);
    out[2] = ~(a[2] & b[2]);
    out[1] = ~(a[1] & b[1]);
    out[0] = ~(a[0] & b[0]);

end


endmodule