module gate_level_mux (
  input in0,
  input in1,
  input sel,
  output out
);

  wire not_sel;
  not (not_sel, sel);

  and a1 (out, in1, sel);
  and a2 (out, in0, not_sel);
  or o1 (out, a1.out, a2.out);

endmodule