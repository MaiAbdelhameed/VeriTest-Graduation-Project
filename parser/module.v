module ConditionalAssignExample(
  input[2:0]  a,
  input[2:0]  b,
  output wire result
);

  // Using assign statement with conditional operator
  assign result = (a > b) ? a : b;

endmodule
