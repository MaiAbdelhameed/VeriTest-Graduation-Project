// tested
module nand15 (
    input wire [2:0] a,
    input wire [2:0] b,
    output reg [2:0] out
);

always @(*) begin
    out[2] = ~(a[2] & b[2]);
    out[1] = ~(a[1] & b[1]);
    out[0] = ~(a[0] & b[0]);

end


endmodule