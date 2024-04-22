module nand_gate2 (
  input a,
  input b,
  output out
);

  nand (out, a, b); // Instantiate a NAND gate primitive

endmodule
