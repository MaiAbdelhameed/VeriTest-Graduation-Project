module pe19 (i3,i2,i1,i0,o0,o1,v);

    input i3,i2,i1,i0;
    output o0,o1,v;
    wire o1_temp;

    assign o0 = (i3) | (i1&~i2);
    assign o1_temp = i3 | i2;
    assign v = o1_temp | i0;
    assign o1 = o1_temp;

endmodule