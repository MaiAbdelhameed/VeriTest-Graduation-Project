// 4 input and
// tested
module and27 (
  input a,
  input b,
  input c,
  input d,
  output out
);

  assign out = &{a,b,c,d}; // Performs an AND operation

endmodule
