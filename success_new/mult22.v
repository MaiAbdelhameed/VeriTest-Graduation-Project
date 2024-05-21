// array multiplier 4x4 - tested
module mult22(a,b,c);
    input [3:0]a, b;
    output [7:0]c;
     
    wire [3:0]q0,q1,q2,q3,q4,temp1;
     
    wire [7:0]c;
    wire [5:0]q5,q6,temp2,temp3,temp4;
     
    // z1
    wire [3:0] tempz1;
     
    assign q0[0]=a[0]&b[0];
    assign tempz1[0]=a[1]&b[0];
    assign tempz1[1]=a[0]&b[1];
    assign tempz1[2]=a[1]&b[1];
    
    assign q0[1] = tempz1[0]^tempz1[1];
    assign tempz1[3] = tempz1[0]&tempz1[1];
    
    assign q0[2] = tempz1[2]^tempz1[3];
    assign q0[3] = tempz1[2]&tempz1[3];

    // z2
    wire [3:0] tempz2;
     
    assign q1[0]=a[2]&b[0];
    assign tempz2[0]=a[3]&b[0];
    assign tempz2[1]=a[2]&b[1];
    assign tempz2[2]=a[3]&b[1];
    
    assign q1[1] = tempz2[0]^tempz2[1];
    assign tempz2[3] = tempz2[0]&tempz2[1];
    
    assign q1[2] = tempz2[2]^tempz2[3];
    assign q1[3] = tempz2[2]&tempz2[3];

    // z3
    wire [3:0] tempz3;
     
    assign q2[0]=a[0]&b[2];
    assign tempz3[0]=a[1]&b[2];
    assign tempz3[1]=a[0]&b[3];
    assign tempz3[2]=a[1]&b[3];
    
    assign q2[1] = tempz3[0]^tempz3[1];
    assign tempz3[3] = tempz3[0]&tempz3[1];
    
    assign q2[2] = tempz3[2]^tempz3[3];
    assign q2[3] = tempz3[2]&tempz3[3];

    // z4
    wire [3:0] tempz4;
     
    assign q3[0]=a[2]&b[2];
    assign tempz4[0]=a[3]&b[2];
    assign tempz4[1]=a[2]&b[3];
    assign tempz4[2]=a[3]&b[3];
    
    assign q3[1] = tempz4[0]^tempz4[1];
    assign tempz4[3] = tempz4[0]&tempz4[1];
    
    assign q3[2] = tempz4[2]^tempz4[3];
    assign q3[3] = tempz4[2]&tempz4[3];
    //
    assign temp1 ={2'b0,q0[3:2]};
    assign q4 = q1[3:0]+temp1;
    assign temp2 ={2'b0,q2[3:0]};
    assign temp3 ={q3[3:0],2'b0};
    assign q5 = temp2+temp3;
    assign temp4={2'b0,q4[3:0]};
    assign q6 = temp4+q5;
     
    assign c[1:0]=q0[1:0];
    assign c[7:2]=q6[5:0];
endmodule