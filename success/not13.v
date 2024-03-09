module not13 (
    input wire a,
    output reg out
);

always @(*) begin
    if (a == 1'b0)
        out = 1'b1;
    else
        out = 1'b0;
end

endmodule
