// tested
module and6_gate (
  input a,
  input b,
  output out
);

  nor (out,~a,~b);

endmodule