// 8 input nor
// tested
module nor20 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  input g,
  input h,
  output out
);

  assign out = ~(a | b | c | d | e | f | g | h);

endmodule
