module and23 (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire [3:0] out
);

assign out = {a[3] & b[3], a[2] & b[2], a[1] & b[1], a[0] & b[0]};

endmodule
