// tested
module nand4_gate (
  input a,
  input b,
  output out
);

  wire not_a, not_b;
  not (not_a, a);
  not (not_b, b);
  or (out, not_a, not_b); // Combine NOT gates with OR gate

endmodule
