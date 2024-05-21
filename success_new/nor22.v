// tested
module nor22 (
  input a,
  input b,
  input c,
  output out
);

  assign out = ~(a | b | c);

endmodule
