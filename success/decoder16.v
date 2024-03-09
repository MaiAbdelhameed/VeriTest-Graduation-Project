module decoder16 (in,out1);
input [2:0] in;
output [7:0] out1;

// Individual wires
assign out1[0] = ~in[2] & ~in[1] & ~in[0];
assign out1[1] = ~in[2] & ~in[1] & in[0];
assign out1[2] = ~in[2] & in[1] & ~in[0];
assign out1[3] = ~in[2] & in[1] & in[0];
assign out1[4] = in[2] & ~in[1] & ~in[0];
assign out1[5] = in[2] & ~in[1] & in[0];
assign out1[6] = in[2] & in[1] & ~in[0];
assign out1[7] = in[2] & in[1] & in[0];

endmodule

