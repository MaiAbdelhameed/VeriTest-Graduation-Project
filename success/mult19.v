module mult19 (
    input [1:0] a,
    input [1:0] b,
    output reg [1:0] result
);

always @(*) begin
    // Bit-wise multiplication
    result[0] = a[0] & b[0];
    result[1] = a[1] & b[0];
end

endmodule
