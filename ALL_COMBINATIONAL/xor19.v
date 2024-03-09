module xor19 (
    input wire a,
    input wire b,
    output wire out
);

reg temp;
always @(*) begin
    if (a ^ b == 1'b1)
        temp = 1'b1;
    else
        temp = 1'b0;
end

assign out = temp;
endmodule
