module mult28 (
    input [2:0] a,
    input [1:0] b,
    output reg [4:0] result
);

always @(*) begin
    result = 5'b0;

    for (int i = 0; i < 2; i = i + 1) begin
        if (b[i] == 1'b1)
            result = result + (a << i);
    end
end

endmodule
