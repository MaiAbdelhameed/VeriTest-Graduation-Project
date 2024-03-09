module nor2 (
  input a,
  input b,
  output out
);

  nor (out, a, b); // Instantiate a NOR gate primitive

endmodule