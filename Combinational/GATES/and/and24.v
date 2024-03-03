module bitwise_and_loop(
    input wire [3:0] a,
    input wire [3:0] b,
    output wire [3:0] out
);

reg [3:0] result;

always @(*) begin
    for (int i = 0; i < 4; i = i + 1) begin
        result[i] = a[i] & b[i];
    end
end

assign out = result;

endmodule
