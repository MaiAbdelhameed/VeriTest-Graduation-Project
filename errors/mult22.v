module mult22 ( // test
    input [1:0] a,
    input [1:0] b,
    output reg [3:0] result
);

integer i;
always @(*) begin
    result = 4'b0;
    for (i = 0; i < 2; i = i + 1) begin
        if (b[i] == 1'b1)
            result = result + (a << i);
    end
end

endmodule

Error occurred: 'ForStatement' object has no attribute 'name'