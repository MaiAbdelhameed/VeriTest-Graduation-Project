module pe17 (i3,i2,i1,i0,o0,o1,v);

    input i3,i2,i1,i0;
    output o0,o1,v;

    assign o0 = (i3) | (i1&~i2);
    assign o1 = i3 | i2;
    assign v = (i3 | i2) | i0;

endmodule