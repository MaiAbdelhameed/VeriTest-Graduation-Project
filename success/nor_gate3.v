module nor_gate3 (
  input a,
  input b,
  output out
);

  wire not_a, not_b;
  not (not_a, a);
  not (not_b, b);
  and (out, not_a, not_b); // Combine NOT gates with AND gate (inverted OR implementation)

endmodule
