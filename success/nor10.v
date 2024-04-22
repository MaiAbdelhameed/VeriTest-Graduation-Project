module nor10 (
    input wire a,
    output wire out
);

assign out = (|a == 1'b0) ? 1'b1 : 1'b0;

endmodule
