module nor_gate4 (
  input a,
  input b,
  output out
);

  assign out = (a == 1'b1 && b == 1'b1) ? 1'b0 : 1'b1; // NOR using conditional expression

endmodule
