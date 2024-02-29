module gate_xnor (
  input a,
  input b,
  output out
);

  xnor (out, a, b); // Instantiate an XNOR gate primitive

endmodule
