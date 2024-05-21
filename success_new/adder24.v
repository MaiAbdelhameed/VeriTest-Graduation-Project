// ripple carry adder 4 bits - tested
module adder24(input [3:0] a,input [3:0] b,input cin,output [3:0] sum,output cout );
wire [2:0]c;

// FA0
assign sum[0] =  a[0] ^ b[0] ^ cin;
assign c  [0] = (a[0] & b[0]) | (cin & b[0]) | (a[0] & cin);

// FA1
assign sum[1] =  a[1] ^ b[1] ^ c[0];
assign c  [1] = (a[1] & b[1]) | (c[0] & b[1]) | (a[1] & c[0]);

// FA2
assign sum[2] =  a[2] ^ b[2] ^   c[1];
assign c  [2] = (a[2] & b[2]) | (c[1] & b[2]) | (a[2] & c[1]);

// FA3
assign sum[3] =  a[3] ^ b[3] ^   c[2];
assign cout = (a[3] & b[3]) | (c[2] & b[3]) | (a[3] & c[2]);

endmodule