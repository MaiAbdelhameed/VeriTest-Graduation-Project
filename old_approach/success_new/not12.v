module not12 (
    input wire a,
    output wire out
);

wire intermediate;
assign intermediate = a & a;
assign out = ~intermediate;

endmodule
