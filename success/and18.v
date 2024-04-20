module and18 (
    input wire a,
    output wire out
);

assign out = &{a};

endmodule
