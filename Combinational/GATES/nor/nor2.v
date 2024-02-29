module gate_nor (
  input a,
  input b,
  output out
);

  nor (out, a, b); // Instantiate a NOR gate primitive

endmodule