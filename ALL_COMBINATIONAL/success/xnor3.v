module xnor3 (
  input a,
  input b,
  output out
);

  xor xor_inst (out_xor, a, b);
  not not_inst (out, out_xor); // NOT the XOR output for XNOR

endmodule
