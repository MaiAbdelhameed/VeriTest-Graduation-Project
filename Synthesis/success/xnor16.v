module xnor16 (
    input wire a,
    input wire b,
    output reg out
);

always @(*) begin
    if (a ^ b == 1'b0)
        out = 1'b1;
    else
        out = 1'b0;
end

endmodule
