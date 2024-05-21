// tested
module nor5_gate (
    input wire a,
    input wire b,
    output wire out
);

assign out = ~(|{a,b});

endmodule
