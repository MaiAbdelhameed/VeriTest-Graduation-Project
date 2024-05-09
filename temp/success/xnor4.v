module xnor4 (
  input a,
  input b,
  output out
);

  assign out = (a == b) ? 1'b1 : 1'b0; // XNOR using conditional expression (XOR and invert both)

endmodule
