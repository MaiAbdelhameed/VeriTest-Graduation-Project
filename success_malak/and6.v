// tested
module and6 (
  input a,
  input b,
  output out
);

  nor (out,~a,~b);

endmodule