module mult17 (
    input [2:0] a,
    input [2:0] b,
    output reg [5:0] result
); // tested

always @(*) begin
    result = 6'b0;

    if (b[0] == 1'b1)
            result = result + (a << 0);

    if (b[1] == 1'b1)
            result = result + (a << 1);

    if (b[2] == 1'b1)
            result = result + (a << 2);

end

endmodule
