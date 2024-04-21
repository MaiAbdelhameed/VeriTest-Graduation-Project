module pe3 (en,i,y);
    // declare port list via input and output
    input en;
    input [7:0]i;
    output [2:0]y;

    wire temp1,temp2,temp3; // temp is used to apply 
                            // enable for the or gates
    // check the logic diagram and use 
    // logic gates to compute outputs
    or o1(temp1,i[4],i[5],i[6],i[7]);
    or o2(temp2,i[2],i[3],i[6],i[7]);
    or o3(temp3,i[1],i[3],i[5],i[7]);

    and a1(y[2],temp1,en);
    and a2(y[1],temp2,en);
    and a3(y[0],temp3,en);

endmodule