module mux_8x1 (
  input wire [7:0] in,
  input wire [2:0] sel,
  output [5:0] out,
  input [5:0] a,
  input [5:0] b
);
assign out[2] = a[0];
assign out[1:0] = a[1:0] & b[3:2];
assign out[5:3] = a[5:3];

endmodule
