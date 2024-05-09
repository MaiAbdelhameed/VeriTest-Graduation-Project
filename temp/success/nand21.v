module nand21 (
    input wire a,
    output reg out
);

wire intermediate;
assign intermediate = a & a;

always @(*) begin
    out = ~intermediate;
end

endmodule
