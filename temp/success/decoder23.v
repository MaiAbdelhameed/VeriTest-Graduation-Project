module decoder23 (in,en,out1);
input [2:0] in;
input en;
output [7:0] out1;

// Individual wires
assign out1[0] = en & ~in[2] & ~in[1] & ~in[0];
assign out1[1] = en & ~in[2] & ~in[1] & in[0];
assign out1[2] = en & ~in[2] & in[1] & ~in[0];
assign out1[3] = en & ~in[2] & in[1] & in[0];
assign out1[4] = en & in[2] & ~in[1] & ~in[0];
assign out1[5] = en & in[2] & ~in[1] & in[0];
assign out1[6] = en & in[2] & in[1] & ~in[0];
assign out1[7] = en & in[2] & in[1] & in[0];

endmodule

