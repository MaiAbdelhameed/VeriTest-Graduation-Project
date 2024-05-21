// wallace multiplier 4x4 - tested
module mult29(A,B,prod);
    
    //inputs and outputs
    input [3:0] A,B;
    output [7:0] prod;
    //internal variables.
    wire s01,s02,s03,s04,s11,s12,s13,s14,s21,s22,s23,s24;
    wire c01,c02,c03,c04,c11,c12,c13,c14,c21,c22,c23,c24;
    wire [6:0] p0,p1,p2,p3;

//initialize the p's.
    assign  p0 = A & {4{B[0]}};
    assign  p1 = A & {4{B[1]}};
    assign  p2 = A & {4{B[2]}};
    assign  p3 = A & {4{B[3]}};

//final product assignments    
    assign prod[0] = p0[0];
    assign prod[1] = s01;
    assign prod[2] = s11;
    assign prod[3] = s21;
    assign prod[4] = s22;
    assign prod[5] = s23;
    assign prod[6] = s24;
    assign prod[7] = c24;

//first stage
    assign {c01,s01} = p0[1]+p1[0];
    assign {c04,s04} = p1[3]+p2[2];
    assign {c02,s02} = p0[2] + p1[1] + p2[0];
    assign {c03,s03} = p0[3] + p1[2] + p2[1];

//second stage
    assign {c11,s11} = c01+s02;
    assign {c12,s12} = p3[0]+c02  +s03  ;
    assign {c13,s13} = c03  +p3[1]+s04  ;
    assign {c14,s14} = c04  +p2[3]+p3[2];

//third stage
    assign {c21,s21} = c11+s12;
    assign {c22,s22} = c12+s13  +c21;
    assign {c23,s23} = c22+s14  +c13;
    assign {c24,s24} = c23+p3[3]+c14;

endmodule