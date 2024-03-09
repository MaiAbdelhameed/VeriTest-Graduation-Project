module nor1 (
  input a,
  input b,
  output out
);

  assign out = ~(a | b); // NOR using built-in operator

endmodule