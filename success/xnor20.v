module xnor20 (
    input wire a,
    output wire out
);

reg temp;
always @(*) begin
    temp = ~(a ^ a);
end

assign out = temp;

endmodule
