// 7 input nand
// tested
module nand25 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  input g,
  output out
);

  assign out = ~(a & b & c & d & e & f & g); // Performs an AND operation

endmodule
