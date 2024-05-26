module pe16 (i3,i2,i1,i0,o0,o1);

    input i3,i2,i1,i0;
    output o0,o1;

    assign o0 = (i3) | (i1&~i2);
    assign o1 = i3 | i2;

endmodule