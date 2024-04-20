module xnor25 (
    input wire a,
    output wire out
);

reg temp;
always @(*) begin
    if (a ^ a == 1'b0)
        temp = 1'b1;
    else
        temp = 1'b0;
end

assign out = temp;

endmodule
