//explicit gates
module gate_or (
  input a,
  input b,
  output out
);

  // Instantiate an OR gate primitive
  or (out, a, b);

endmodule