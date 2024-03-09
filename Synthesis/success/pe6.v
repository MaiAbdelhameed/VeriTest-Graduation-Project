module pe6 (i,y);
    // declare port list via input and output
    input [7:0]i;
    output [2:0]y;

    // check the logic diagram and use 
    // logic gates to compute outputs
    or o1(y[2],i[4],i[5],i[6],i[7]);
    or o2(y[1],i[2],i[3],i[6],i[7]);
    or o3(y[0],i[1],i[3],i[5],i[7]);

endmodule