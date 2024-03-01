module mult25(
    input [3:0] a,
    input [3:0] b,
    output reg [7:0] result
);

reg [3:0] partial_products [3:0];
reg [7:0] result_temp;

always @(*) begin
    for (int i = 0; i < 4; i = i + 1) begin
        partial_products[i] = a & (b[i] ? {4'b0, a} : 4'b0);
    end
    result_temp = partial_products[0] + (partial_products[1] << 1) + (partial_products[2] << 2) + (partial_products[3] << 3);
    result = result_temp;
end

endmodule
