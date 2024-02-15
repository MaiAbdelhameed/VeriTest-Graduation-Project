module gate_and (
  input a,
  input b,
  output out
);

  // Instantiate an AND gate primitive
  and (out, a, b);

endmodule
