// tested
module and7_gate (
  input a,
  input b,
  output out
);

wire temp;
  or (temp,~a,~b);
  not(out,temp);

endmodule