module xor27 (
    input wire [3:0] a,
    output wire out
);

reg temp;
always @(*) begin
    if (^a == 1'b1)
        temp = 1'b1;
    else
        temp = 1'b0;
end

endmodule
