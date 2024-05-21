// 3 input nand
// tested
module nand21 (
  input a,
  input b,
  input c,
  output out
);

  assign out = ~(a & b & c);

endmodule
