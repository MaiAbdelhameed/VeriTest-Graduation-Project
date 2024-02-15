module simple_xnor (
  input a,
  input b,
  output out
);

  assign out = a ^~ b; // XNOR using built-in operator

endmodule
