// ripple carry adder 16 bits - tested
module adder23(input [15:0] a,input [15:0] b,input cin,output [15:0] sum,output cout );
wire [14:0]c;

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
assign c  [3] = (a[3] & b[3]) | (c[2] & b[3]) | (a[3] & c[2]);

// FA4
assign sum[4] =  a[4] ^ b[4] ^   c[3];
assign c  [4] = (a[4] & b[4]) | (c[3] & b[4]) | (a[4] & c[3]);

// FA5
assign sum[5] =  a[5] ^ b[5] ^   c[4];
assign c  [5] = (a[5] & b[5]) | (c[4] & b[5]) | (a[5] & c[4]);

// FA6
assign sum[6] =  a[6] ^ b[6] ^   c[5];
assign c  [6] = (a[6] & b[6]) | (c[5] & b[6]) | (a[6] & c[5]);

// FA7
assign sum[7] =  a[7] ^ b[7] ^   c[6];
assign c[7] = (a[7] & b[7]) | (c[6] & b[7]) | (a[7] & c[6]);

// FA8
assign sum[8] =  a[8] ^ b[8] ^ c[7];
assign c  [8] = (a[8] & b[8]) | (c[7] & b[8]) | (a[8] & c[7]);

// FA9
assign sum[9] =  a[9] ^ b[9] ^ c[8];
assign c  [9] = (a[9] & b[9]) | (c[8] & b[9]) | (a[9] & c[8]);

// FA10
assign sum[10] =  a[10] ^ b[10] ^   c[9];
assign c  [10] = (a[10] & b[10]) | (c[9] & b[10]) | (a[10] & c[9]);

// FA11
assign sum[11] =  a[11] ^ b[11] ^   c[10];
assign c  [11] = (a[11] & b[11]) | (c[10] & b[11]) | (a[11] & c[10]);

// FA12
assign sum[12] =  a[12] ^ b[12] ^   c[11];
assign c  [12] = (a[12] & b[12]) | (c[11] & b[12]) | (a[12] & c[11]);

// FA13
assign sum[13] =  a[13] ^ b[13] ^   c[12];
assign c  [13] = (a[13] & b[13]) | (c[12] & b[13]) | (a[13] & c[12]);

// FA14
assign sum[14] =  a[14] ^ b[14] ^   c[13];
assign c  [14] = (a[14] & b[14]) | (c[13] & b[14]) | (a[14] & c[13]);

// FA7
assign sum[15] =  a[15] ^ b[15] ^   c[14];
assign cout = (a[15] & b[15]) | (c[14] & b[15]) | (a[15] & c[14]);

endmodule