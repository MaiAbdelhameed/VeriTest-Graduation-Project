module behavioral_half_adder (
  input a,
  input b,
  output sum,
  output carry
);

  assign sum = (a == b) ? 0 : 1;
  assign carry = (a & b) ? 1 : 0;

endmodule
