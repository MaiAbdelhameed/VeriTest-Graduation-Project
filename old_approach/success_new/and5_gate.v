// tested
module and5_gate (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b0 || b == 1'b0) ? 1'b0 : 1'b1;

endmodule