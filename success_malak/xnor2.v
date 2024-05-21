module xnor2 (
  input a,
  input b,
  output out
);

  xnor (out, a, b); // Instantiate an XNOR gate primitive

endmodule
