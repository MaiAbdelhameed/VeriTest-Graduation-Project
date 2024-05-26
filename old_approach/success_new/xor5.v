// tested
module xor5 (
    input wire a,b,
    output wire out
);

assign out = ^{a,b};

endmodule
