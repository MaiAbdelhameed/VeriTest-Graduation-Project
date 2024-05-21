
// tested
module nor28 (
  input a,
  input b,
  input c,
  input d,
  input e,
  input f,
  input g,
  input h,
  input a1,
  input b1,
  input c1,
  input d1,
  input e1,
  input f1,
  input g1,
  input h1,
  output out
);

  assign out = ~(a | b | c | d | e | f | g | h | a1 | b1 | c1 | d1 | e1 | f1 | g1 | h1);

endmodule
