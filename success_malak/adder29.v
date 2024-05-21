// ma haza
module adder29(input [7:0]b,input [7:0]c,input [7:0]d,input [7:0]e,output [8:0]sum,output cout);
wire [7:0]s0,c0,c1;
wire [6:0]cw,s1;

// fa0
assign s0[0] =  s1[0] ^ c[0] ^ d[0];
assign c0[0] = (s1[0] & c[0]) | (d[0] & c[0]) | (s1[0] & d[0]);

// fa1
assign s0[1] =  s1[1] ^ c[1] ^   d[1];
assign c0[1] = (s1[1] & c[1]) | (d[1] & c[1]) | (s1[1] & d[1]);

// fa2
assign s0[2] =  s1[2] ^ c[2] ^   d[2];
assign c0[2] = (s1[2] & c[2]) | (d[2] & c[2]) | (s1[2] & d[2]);

// fa3
assign s0[3] =  s1[3] ^ c[3] ^   d[3];
assign c0[3] = (s1[3] & c[3]) | (d[3] & c[3]) | (s1[3] & d[3]);

// fa4
assign s0[4] =  s1[4] ^ c[4] ^   d[4];
assign c0[4] = (s1[4] & c[4]) | (d[4] & c[4]) | (s1[4] & d[4]);

// fa5
assign s0[5] =  s1[5] ^ c[5] ^   d[5];
assign c0[5] = (s1[5] & c[5]) | (d[5] & c[5]) | (s1[5] & d[5]);

// fa6
assign s0[6] =  s1[6] ^ c[6] ^   d[6];
assign c0[6] = (s1[6] & c[6]) | (d[6] & c[6]) | (s1[6] & d[6]);

// fa7
assign s0[7] =  s1[7] ^ c[7] ^   d[7];
assign c0[7] = (s1[7] & c[7]) | (d[7] & c[7]) | (s1[7] & d[7]);

//

// fa8
assign sum[0] =  e[0] ^ s0[0] ^   1'b0;
assign c1 [0] = (e[0] & s0[0]) | (1'b0 & s0[0]) | (e[0] & 1'b0);

// fa9
assign s1[0] =  e[1] ^ s0[1] ^   c0[0];
assign c1[1] = (e[1] & s0[1]) | (c0[0] & s0[1]) | (e[1] & c0[0]);

// fa10
assign s1[1] =  e[2] ^ s0[2] ^   c0[1];
assign c1[2] = (e[2] & s0[2]) | (c0[1] & s0[2]) | (e[2] & c0[1]);

// fa11
assign s1[2] =  e[3] ^ s0[3] ^   c0[2];
assign c1[3] = (e[3] & s0[3]) | (c0[2] & s0[3]) | (e[3] & c0[2]);

// fa12
assign s1[3] =  e[4] ^ s0[4] ^   c0[3];
assign c1[4] = (e[4] & s0[4]) | (c0[3] & s0[4]) | (e[4] & c0[3]);

// fa13
assign s1[4] =  e[5] ^ s0[5] ^   c0[4];
assign c1[5] = (e[5] & s0[5]) | (c0[4] & s0[5]) | (e[5] & c0[4]);

// fa14
assign s1[5] =  e[6] ^ s0[6] ^   c0[5];
assign c1[6] = (e[6] & s0[6]) | (c0[5] & s0[6]) | (e[6] & c0[5]);

// fa15
assign s1[6] =  e[7] ^ s0[7] ^   c0[7];
assign c1[7] = (e[7] & s0[7]) | (c0[7] & s0[7]) | (e[7] & c0[7]);

// 8 bit ripple carry

wire [6:0]c;

// FA0
assign sum[1] =  c1[0] ^ s1[0] ^ 1'b0;
assign c  [0] = (c1[0] & s1[0]) | (1'b0 & s1[0]) | (c1[0] & 1'b0);

// FA1
assign sum[2] =  c1[1] ^ s1[1] ^ c[0];
assign c  [1] = (c1[1] & s1[1]) | (c[0] & s1[1]) | (c1[1] & c[0]);

// FA2
assign sum[3] =  c1[2] ^ s1[2] ^   c[1];
assign c  [2] = (c1[2] & s1[2]) | (c[1] & s1[2]) | (c1[2] & c[1]);

// FA3
assign sum[4] =  c1[3] ^ s1[3] ^   c[2];
assign c  [3] = (c1[3] & s1[3]) | (c[2] & s1[3]) | (c1[3] & c[2]);

// FA4
assign sum[5] =  c1[4] ^ s1[4] ^   c[3];
assign c  [4] = (c1[4] & s1[4]) | (c[3] & s1[4]) | (c1[4] & c[3]);

// FA5
assign sum[6] =  c1[5] ^ s1[5] ^   c[4];
assign c  [5] = (c1[5] & s1[5]) | (c[4] & s1[5]) | (c1[5] & c[4]);

// FA6
assign sum[7] =  c1[6] ^ s1[6] ^   c[5];
assign c  [6] = (c1[6] & s1[6]) | (c[5] & s1[6]) | (c1[6] & c[5]);

// FA7
assign sum[8] =  c1[7] ^ c0[7] ^   c[6];
assign cout = (c1[7] & c0[7]) | (c[6] & c0[7]) | (c1[7] & c[6]);

endmodule