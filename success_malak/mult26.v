// array multiplier 4x4 - tested
module mult26(
input [3:0]x,
input [3:0]y,
output [7:0]out
    );
    wire p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14;
    wire c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10;
    wire o1,o2,o3,o4,o5,o6;
    and(out[0],x[0],y[0]);
    and(p0,x[1],y[0]);
    and(p1,x[0],y[1]);
    assign {c0,out[1]} = p0 + p1; // ha
    and(p2,x[2],y[0]);
    and(p3,x[1],y[1]);
    and(p4,x[0],y[2]);
    assign {c1,o1} = p2 + p3 + c0; // fa
    assign {c2,out[2]} = p4 + o1; // ha
    and(p5,x[3],y[0]);
    and(p6,x[2],y[1]);
    and(p7,x[1],y[2]);
    and(p8,x[0],y[3]);
    assign {c3,o2} = p5 + p6 + c1; // fa
    assign {c4,o3} = o2 + p7 + c2; // fa
    assign {c5,out[3]} = o3 + p8; // ha
    and(p9,x[3],y[1]);
    and(p10,x[2],y[2]);
    and(p11,x[1],y[3]);
    assign {c6,o4} = p9 + c3;
    assign {c7,o5} = p10 + o4 + c4;
    assign {c8,out[4]} = o5 + p11 + c5;
    and(p12,x[3],y[2]);
    and(p13,x[2],y[3]);
    assign {c9,o6} = p12 + c6 + c7;
    assign {c10,out[5]} = p13 + o6 + c8;
    and(p14,x[3],y[3]);
    assign {out[7],out[6]} = p14 + c9 + c10;
endmodule