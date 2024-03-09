//explicit gates
module or_gate2 (
  input a,
  input b,
  output out
);

  // Instantiate an OR gate primitive
  or (out, a, b);

endmodule