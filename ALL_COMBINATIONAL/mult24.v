module mult24 (
    input [3:0] a,
    input [3:0] b,
    output reg [7:0] result
);

integer i;

always @(*) begin
    result = 8'b0;

    for (i = 0; i < 4; i = i + 1) begin
        if (b[i] == 1'b1)
            result = result + (a << i);
    end
end

endmodule
