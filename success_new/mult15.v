module mult15 (
    input [3:0] a,
    input [3:0] b,
    output reg [7:0] result
); // tested


always @(*) begin
    result = 8'b0;

    if (b[0] == 1'b1)
            result = result + (a << 0);
    if (b[1] == 1'b1)
            result = result + (a << 1);
    if (b[2] == 1'b1)
            result = result + (a << 2);
    if (b[3] == 1'b1)
            result = result + (a << 3);
end

endmodule
