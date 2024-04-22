module xor3 (
  input a,
  input b,
  output out
);

  assign out = (a == b) ? 1'b0 : 1'b1; // Check if bits are equal

endmodule