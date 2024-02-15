module assign_mux (
  input in0,
  input in1,
  input sel,
  output out
);

  assign out = (sel & in1) | (~sel & in0);

endmodule