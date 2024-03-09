module pe14 (en,i0,i1,i2,i3,i4,i5,i6,i7,y0,y1,y2);
    // declare port list via input and output
    input en;
    input i0,i1,i2,i3,i4,i5,i6,i7;
    output y0,y1,y2;

    wire temp1,temp2,temp3; // temp is used to apply 
                            // enable for the or gates
    // check the logic diagram and use 
    // logic gates to compute outputs
    or o1(temp1,i4,i5,i6,i7);
    or o2(temp2,i2,i3,i6,i7);
    or o3(temp3,i1,i3,i5,i7);

    and a1(y2,temp1,en);
    and a2(y1,temp2,en);
    and a3(y0,temp3,en);

endmodule