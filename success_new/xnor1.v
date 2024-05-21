module xnor1 (
  input a,
  input b,
  output out
);

  wire xor_out;

  xor (xor_out,a,b);

  assign out = ~xor_out;

endmodule
