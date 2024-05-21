module not3 (
  input in,
  output out
);

  assign out = (in == 1'b0) ? 1'b1 : 1'b0; // Check for 0 and invert

endmodule
