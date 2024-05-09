//conditional expressions
module or_gate4 (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b0 && b == 1'b0) ? 1'b0 : 1'b1; // Check both bits are low

endmodule
