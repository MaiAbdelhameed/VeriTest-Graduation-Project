module pe22 (i3,i2,i1,i0,en,o0,o1);

    input i3,i2,i1,i0,en;
    output o0,o1;

    assign o0 = en & ((i3) | (i1&~i2));
    assign o1 = en & (i3 | i2);

endmodule