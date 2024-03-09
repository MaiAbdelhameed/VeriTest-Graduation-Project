module mult20 ( //test
    input [1:0] a,
    input [1:0] b,
    output reg [3:0] result
);

reg [3:0] g, p, c;

always @(*) begin
    g = a[0] & b[0];
    p = a[0] ^ b[0];
    c[0] = 1'b0;

    g = g + (a[1] & b[1]);
    p = p ^ (a[1] & b[1]);
    c[1] = g | (a[1] & b[1]);

    g = g + (p[0] & c[0]);
    p = p ^ (p[0] & c[0]);
    c[2] = g | (p[0] & c[0]);

    g = g + (p[1] & c[1]);
    p = p ^ (p[1] & c[1]);
    c[3] = g | (p[1] & c[1]);

    result = {c[3], p[1], p[0], g};
end

endmodule
