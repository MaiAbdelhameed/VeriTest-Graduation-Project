module nand_gate4 (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b0 || b == 1'b0) ? 1'b1 : 1'b0; // NAND using conditional expression

endmodule
