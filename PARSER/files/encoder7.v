module encoder7 (y,a);
    input [3:0] y;
    output [1:0] a;

    assign a[0] = y[3] | y[1];
    assign a[1] = y[3] | y[2];

endmodule