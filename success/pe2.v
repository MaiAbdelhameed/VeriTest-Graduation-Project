module pe2 (en,i,y);
    // declare port list via input and output
    input en;
    input [7:0]i;
    output [2:0]y;

    // check the logic diagram and assign the outputs
    assign y[2]=i[4] | i[5] | i[6] | i[7] &en;
    assign y[1]=i[2] | i[3] | i[6] | i[7] &en;
    assign y[0]=i[1] | i[3] | i[5] | i[7] &en;

endmodule