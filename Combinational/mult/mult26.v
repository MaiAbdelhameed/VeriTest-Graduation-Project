module mult26(
    input [2:0] a,
    input [2:0] b,
    output reg [5:0] result
);

always @(*) begin
    result = 6'b0;

    for (int i = 0; i < 3; i = i + 1) begin
        if (b[i] == 1'b1)
            result = result + (a << i);
    end
end

endmodule
