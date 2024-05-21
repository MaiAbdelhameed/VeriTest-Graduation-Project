module mult30 ( //Dataflow
    input [1:0] a,
    input [1:0] b,
    output [3:0] product
);

    assign product[0] = a[0] * b[0];
    assign product[1] = a[0] * b[1] + a[1] * b[0];
    assign product[2] = a[1] * b[1];
    assign product[3] = 0; // Most significant bit is always 0 for unsigned multiplication

endmodule
