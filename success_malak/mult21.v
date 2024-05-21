// array multiplier 2x2
module mult21(a, b, c); // tested
    input [1:0]a, b;
    output [3:0]c;
    wire [3:0]c, temp;

    assign c[0]=a[0]&b[0];
    assign temp[0]=a[1]&b[0];
    assign temp[1]=a[0]&b[1];
    assign temp[2]=a[1]&b[1];
    
    assign c[1] = temp[0]^temp[1];
    assign temp[3] = temp[0]&temp[1];
    
    assign c[2] = temp[2]^temp[3];
    assign c[3] = temp[2]&temp[3];

endmodule