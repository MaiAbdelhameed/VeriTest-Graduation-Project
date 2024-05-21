// 8 input nor
// tested
module nor23 (
  input a,
  input b,
  input c,
  input d,
  input e,
  output out
);

  assign out = ~(a | b | c | d | e);

endmodule
