// 5 input nand
// tested
module nand23 (
  input a,
  input b,
  input c,
  input d,
  input e,
  output out
);

  assign out = ~(a & b & c & d & e);

endmodule
