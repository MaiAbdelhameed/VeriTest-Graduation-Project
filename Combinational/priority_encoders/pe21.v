module pe21 (i,en,o,v);

    input en;
    input [3:0] i;
    output [1:0] o; 
    output v;

    assign o[0] = ((i[3]) | (i[1]&~i[2])) & en;
    assign o[1] = (i[3] | i[2]) &en;
    assign v = ((i[3] | i[2]) | i[0]) &en;

endmodule