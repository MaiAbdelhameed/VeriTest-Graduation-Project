// tested
module and3_gate (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b1 && b == 1'b1) ? 1'b1 : 1'b0; // Check both bits are high

endmodule