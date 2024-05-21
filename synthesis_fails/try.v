module top_module(
    input [7:0] in1,
    input [7:0] in2,
    output [15:0] prod);
    
    //Array to store partial products-----------------------------
    reg [7:0] part_prod0;
    reg [7:0] part_prod1;
    reg [7:0] part_prod2;
    reg [7:0] part_prod3;
    reg [7:0] part_prod4;
    reg [7:0] part_prod5;
    reg [7:0] part_prod6;
    reg [7:0] part_prod7;

    reg [7:0] a, b;
    wire [9:0] p1, p2, p4, c5;
    wire [10:0] c6;
    wire [7:0] c1, c2, c3, c4;
    wire [15:0] p7;
    wire [14:0] p5, p6;
    wire [12:0] p3;
    
    always @(*)
        begin
            if(in1>in2)
            begin
            a= in1;
            b= in2;
            end
            else if(in2>in1)
            begin
            a= in2;
            b= in1;
            end
            else
            begin
            a= in1;
            b= in2; 
            end 
        end

    //Loop for storing partial products---------------------------
    always @(*)
        begin
            if(b[0]==0)
                        begin
                        part_prod0<= 8'd0;
                        end
                    else
                        begin
                        part_prod0<= a;
                        end
            
            if(b[1]==0)
                        begin
                        part_prod1<= 8'd0;
                        end
                    else
                        begin
                        part_prod1<= a;
                        end
            
            if(b[2]==0)
                        begin
                        part_prod2<= 8'd0;
                        end
                    else
                        begin
                        part_prod2<= a;
                        end

            if(b[3]==0)
                        begin
                        part_prod3<= 8'd0;
                        end
                    else
                        begin
                        part_prod3<= a;
                        end

            if(b[4]==0)
                        begin
                        part_prod4<= 8'd0;
                        end
                    else
                        begin
                        part_prod4<= a;
                        end

            if(b[5]==0)
                        begin
                        part_prod5<= 8'd0;
                        end
                    else
                        begin
                        part_prod5<= a;
                        end

            if(b[6]==0)
                        begin
                        part_prod6<= 8'd0;
                        end
                    else
                        begin
                        part_prod6<= a;
                        end

            if(b[7]==0)
                        begin
                        part_prod7<= 8'd0;
                        end
                    else
                        begin
                        part_prod7<= a;
                        end
        end
    
    //for 1st group of 3 i.e partial product 0 to 2--------------
    
    assign p1[0]= part_prod0[0];
    assign {c1[0],p1[1]} = part_prod0[1] + part_prod1[0];
    assign {c1[7],p1[8]} = part_prod1[7] + part_prod2[6];
    assign {c1[1],p1[2]} = part_prod0[2] + part_prod1[1] + part_prod2[0];
    assign {c1[2],p1[3]} = part_prod0[3] + part_prod1[2] + part_prod2[1];  
    assign {c1[3],p1[4]} = part_prod0[4] + part_prod1[3] + part_prod2[2];
    assign {c1[4],p1[5]} = part_prod0[5] + part_prod1[4] + part_prod2[3];
    assign {c1[5],p1[6]} = part_prod0[6] + part_prod1[5] + part_prod2[4];
    assign {c1[6],p1[7]} = part_prod0[7] + part_prod1[6] + part_prod2[5];
    assign p1[9]= part_prod[2][7];
    //----------------------------------------------------------
                    
                    
    //for 2nd group of 3 i.e partial product 3 to 5--------------
    assign {c2[1],p2[2]} = part_prod3[2] + part_prod4[1] + part_prod5[0];
    assign {c2[2],p2[3]} = part_prod3[3] + part_prod4[2] + part_prod5[1];
    assign {c2[3],p2[4]} = part_prod3[4] + part_prod4[3] + part_prod5[2];
    assign {c2[4],p2[5]} = part_prod3[5] + part_prod4[4] + part_prod5[3];
    assign {c2[5],p2[6]} = part_prod3[6] + part_prod4[5] + part_prod5[4];
    assign {c2[6],p2[7]} = part_prod3[7] + part_prod4[6] + part_prod5[5];

    
    assign p2[0]= part_prod3[0];
    assign p2[9]= part_prod5[7];

    assign {c2[0],p2[1]} = part_prod3[1] + part_prod4[0];
    assign {c2[7],p2[8]} = part_prod4[7] + part_prod5[6];
    //----------------------------------------------------------                          
    
    //Stage 3

    assign {c4[1],p4[2]} =  c2[2] + part_prod6[1] + part_prod7[0];
    assign {c4[2],p4[3]} =  c2[3] + part_prod6[2] + part_prod7[1];
    assign {c4[3],p4[4]} =  c2[4] + part_prod6[3] + part_prod7[2];
    assign {c4[4],p4[5]} =  c2[5] + part_prod6[4] + part_prod7[3];
    assign {c4[5],p4[6]} =  c2[6] + part_prod6[5] + part_prod7[4];
    assign {c4[6],p4[7]} =  c2[7] + part_prod6[6] + part_prod7[5];
    
    
    assign p4[0]= c2[0];
    assign p4[9]= part_prod7[7];
    assign {c4[0],p4[1]} = c2[1] + part_prod6[0];
    assign {c4[7],p4[8]} = part_prod6[7] + part_prod7[6];
    
     // for p3 and c3                         
    
    assign p3[1:0]= p1[1:0];
    assign p3[12:10]= p2[9:7];
    assign {c3[0],p3[2]} = p1[2] + c1[0];

    assign {c3[1],p3[3]} = p1[3] + c1[1] + p2[0];
    assign {c3[2],p3[4]} = p1[4] + c1[2] + p2[1];
    assign {c3[3],p3[5]} = p1[5] + c1[3] + p2[2];
    assign {c3[4],p3[6]} = p1[6] + c1[4] + p2[3];
    assign {c3[5],p3[7]} = p1[7] + c1[5] + p2[4];
    assign {c3[6],p3[8]} = p1[8] + c1[6] + p2[5];
    assign {c3[7],p3[9]} = p1[9] + c1[7] + p2[6];
    assign {c3[8],p3[10]} = p1[10] + c1[8] + p2[7];


    // for p5 and c5                
    
    assign p5[2:0]= p3[2:0];
    assign p5[14:13]= p4[9:8];
    assign {c5[0],p5[3] } = p3[3] + c3[0];
    assign {c5[1],p5[4]} = p3[4] + c3[1];
    assign {c5[8],p5[11]} = p3[11] + p4[6];
    assign {c5[9],p5[12]} = p3[12] + p4[7];

    assign {c5[2],p5[5]} = p3[5] + c3[2] + p4[0];
    assign {c5[3],p5[6]} = p3[6] + c3[3] + p4[1];
    assign {c5[4],p5[7]} = p3[7] + c3[4] + p4[2];
    assign {c5[5],p5[8]} = p3[8] + c3[5] + p4[3];
    assign {c5[6],p5[9]} = p3[9] + c3[6] + p4[4];
    assign {c5[7],p5[10]} = p3[10] + c3[7] + p4[5];


    //for p6 and c6
    assign p6[3:0]= p5[3:0];
    assign {c6[0],p6[4]} = p5[4]  + c5[0];
    assign {c6[1],p6[5]} = p5[5]  + c5[1];
    assign {c6[2],p6[6]} = p5[6]  + c5[2];
    assign {c6[10],p6[14]} = p5[14] + c4[7];
    
    assign {c6[3],p6[7]} = p5[7] + c5[3] + c4[0];
    assign {c6[4],p6[8]} = p5[8] + c5[4] + c4[1];
    assign {c6[5],p6[9]} = p5[9] + c5[5] + c4[2];
    assign {c6[6],p6[10]} = p5[10] + c5[6] + c4[3];
    assign {c6[7],p6[11]} = p5[11] + c5[7] + c4[4];
    assign {c6[8],p6[12]} = p5[12] + c5[8] + c4[5];
    assign {c6[9],p6[13]} = p5[13] + c5[9] + c4[6];

                    
    assign p7= {c6,5'b00000};
    assign prod= p6 + p7;
                    
endmodule

module ha (
           input a,
           input b,
           output s,
           output c);
    assign s= a^b;
    assign c= a&b;
    
endmodule

module fa (
    input a,
    input b,
    input cin,
    output s,
    output cout);
    
    assign s= a^b^cin;
    assign cout= a&b | b&cin | cin&a;
endmodule