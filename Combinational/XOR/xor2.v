module xor2 (
  input a,
  input b,
  output out
);

  // Instantiate an XOR gate primitive
  xor (out, a, b);

endmodule