module xor26 (
    input wire [3:0] a,
    output reg out
);

always @(*) begin
    if (^a == 1'b1)
        out = 1'b1;
    else
        out = 1'b0;
end

endmodule
