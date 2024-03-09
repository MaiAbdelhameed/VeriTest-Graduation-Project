module xnor1 (
  input a,
  input b,
  output out
);

  assign out = a ^ ~b; // XNOR using built-in operator

endmodule
