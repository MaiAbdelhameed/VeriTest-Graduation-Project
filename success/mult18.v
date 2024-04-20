module mult18 (
    input [2:0] a,
    input [2:0] b,
    output reg [2:0] result
);

always @(*) begin
    result[0] = a[0] & b[0];
    result[1] = a[1] & b[0];
    result[2] = a[2] & b[0];
end

endmodule
