// 3 input and
// tested
module and26 (
  input a,
  input b,
  input c,
  output out
);

  assign out = &{a,b,c}; // Performs an AND operation

endmodule
