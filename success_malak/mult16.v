module mult16 (
    input [3:0] a,
    input [3:0] b,
    output reg [7:0] result
); //tested

reg [3:0] partial_products0,partial_products1,partial_products2,partial_products3;
reg [7:0] result_temp;

always @(*) begin
    partial_products0 = a & (b[0] ? {4'b0, a} : 4'b0);
    partial_products1 = a & (b[1] ? {4'b0, a} : 4'b0);
    partial_products2 = a & (b[2] ? {4'b0, a} : 4'b0);
    partial_products3 = a & (b[3] ? {4'b0, a} : 4'b0);
    result_temp = partial_products0 + (partial_products1 << 1) + (partial_products2 << 2) + (partial_products3 << 3);
    result = result_temp;
end

endmodule
