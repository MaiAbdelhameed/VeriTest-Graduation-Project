module encoder12 (y,a,en);
    input [3:0] y;
    input en;
    output [1:0] a;

    assign a[0] = en & (y[3] | y[1]);
    assign a[1] = en & (y[3] | y[2]);

endmodule