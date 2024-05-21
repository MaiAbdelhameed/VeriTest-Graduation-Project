module mult19 (
    input [2:0] a,
    input [1:0] b,
    output reg [4:0] result
); // tested

always @(*) begin
    result = 5'b0;
    if (b[0] == 1'b1)
            result = result + (a << 0);
    if (b[1] == 1'b1)
            result = result + (a << 1);
end

endmodule
