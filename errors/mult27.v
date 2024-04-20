module mult27 (
    input [2:0] a,
    input [2:0] b,
    output reg [5:0] result
);

reg [2:0] partial_products [2:0];
reg [5:0] result_temp;
integer i;

always @(*) begin
    for (i = 0; i < 3; i = i + 1) begin
        partial_products[i] = a & (b[i] ? {3'b0, a} : 3'b0);
    end
    result_temp = partial_products[0] + (partial_products[1] << 1) + (partial_products[2] << 2);
    result = result_temp;
end

endmodule

Error occurred: 'ForStatement' object has no attribute 'name'