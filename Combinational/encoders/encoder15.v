module encoder15 (input en,
input [7:0] D,
output [2:0] y);

assign y[2] = en & (D[4] | D[5] | D[6] | D[7]);
assign y[1] = en & (D[2] | D[3] | D[6] | D[7]);
assign y[0] = en & (D[1] | D[3] | D[5] | D[7]);
endmodule