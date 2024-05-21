module mult14 ( // tested
    input [1:0] a,
    input [1:0] b,
    output reg [3:0] result
);

always @(*) begin
    result = 4'b0;
    if (b[0] == 1'b1)
            result = result + (a << 0);
    if (b[1] == 1'b1)
            result = result + (a << 1);
end

endmodule
