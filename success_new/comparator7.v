module comparator7 (
    input a,
    input b,
    output reg eq,
    output reg greater,
    output reg less
);

    always @(*) begin
        eq = (a == b);
        greater = (a > b);
        less = (a < b);
    end

endmodule