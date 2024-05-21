module d_flip_flop_primitive (
  input d,
  input clk,
  output q
);

  dff #(1) dff_inst (.d(d), .clk(clk), .q(q));

endmodule
