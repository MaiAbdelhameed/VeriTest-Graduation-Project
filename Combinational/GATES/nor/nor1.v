module simple_nor (
  input a,
  input b,
  output out
);

  assign out = ~(a | b); // NOR using built-in operator

endmodule