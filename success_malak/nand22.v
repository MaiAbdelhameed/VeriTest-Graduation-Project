// 4 input nand
// tested
module nand22 (
  input a,
  input b,
  input c,
  input d,
  output out
);

  assign out = ~(a & b & c & d);

endmodule
