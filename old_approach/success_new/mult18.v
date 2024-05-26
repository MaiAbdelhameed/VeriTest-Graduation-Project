module mult18 (
    input [2:0] a,
    input [2:0] b,
    output reg [5:0] result
);

reg [2:0] partial_products0,partial_products1,partial_products2;
reg [5:0] result_temp;

always @(*) begin

    partial_products0 = a & (b[0] ? {3'b0, a} : 3'b0);
    partial_products1 = a & (b[1] ? {3'b0, a} : 3'b0);
    partial_products2 = a & (b[2] ? {3'b0, a} : 3'b0);
    result_temp = partial_products0 + (partial_products1 << 1) + (partial_products2 << 2);
    result = result_temp;
end

endmodule
