module mux_8x1 (
  input wire [7:0] in,
  input wire [2:0] sel1,sel2,
  output wire out
);

assign out = (sel1 > sel2 | sel1 == sel2) ? 1'b1 : 1'b0;
endmodule
