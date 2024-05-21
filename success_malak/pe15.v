module pe15 (i0,i1,i2,i3,i4,i5,i6,i7,y0,y1,y2);
    // declare port list via input and output
    input i0,i1,i2,i3,i4,i5,i6,i7;
    output y0,y1,y2;
    // check the logic diagram and use 
    // logic gates to compute outputs
    or o1(y2,i4,i5,i6,i7);
    or o2(y1,i2,i3,i6,i7);
    or o3(y0,i1,i3,i5,i7);

endmodule