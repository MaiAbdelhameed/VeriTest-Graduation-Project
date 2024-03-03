module unary_and_reduction(
    input wire a,
    output wire out
);

assign out = &{a};

endmodule
