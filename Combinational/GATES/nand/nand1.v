module simple_nand (
  input a,
  input b,
  output out
);

  assign out = ~(a & b); // NAND using built-in operator

endmodule
