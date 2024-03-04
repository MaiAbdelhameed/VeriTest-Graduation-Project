module mult29 (
    input [2:0] a,
    input [1:0] b,
    output reg [4:0] result
);

reg [2:0] partial_products [1:0];
reg [4:0] result_temp;

always @(*) begin
    for (int i = 0; i < 2; i = i + 1) begin
        partial_products[i] = a & (b[i] ? {2'b0, a} : 2'b0);
    end
    result_temp = partial_products[0] + (partial_products[1] << 2);
    result = result_temp;
end

endmodule
