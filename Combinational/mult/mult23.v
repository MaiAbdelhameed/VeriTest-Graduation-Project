module mult23 ( //test
    input [1:0] a,
    input [1:0] b,
    output reg [3:0] result
);

reg [3:0] ac;
integer i;

always @(*) begin
    ac = {a[1], a};

    for (i = 0; i < 2; i = i + 1) begin
        if (b[i] == 1'b0)
            ac = {1'b0, ac[3:1]};
        else if (b[i] == 1'b1 && ac[0] == 1'b0)
            ac = ac + {b[i], 2'b0};
        else if (b[i] == 1'b1 && ac[0] == 1'b1)
            ac = ac + {~b[i], 2'b0};
    end

    result = ac[3:0];
end

endmodule
