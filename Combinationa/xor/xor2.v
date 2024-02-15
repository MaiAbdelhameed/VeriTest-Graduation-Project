module gate_xor (
  input a,
  input b,
  output out
);

  // Instantiate an XOR gate primitive
  xor (out, a, b);

endmodule