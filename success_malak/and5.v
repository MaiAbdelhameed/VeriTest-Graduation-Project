// tested
module and5 (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b0 || b == 1'b0) ? 1'b0 : 1'b1;

endmodule