module gate_nand (
  input a,
  input b,
  output out
);

  nand (out, a, b); // Instantiate a NAND gate primitive

endmodule
