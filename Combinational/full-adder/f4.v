module behavioral_full_adder (
  input a,
  input b,
  input cin,
  output sum,
  output cout
);

  assign sum = (a == b) ? cin : (a ^ b);
  assign cout = (a & b) | (b & cin) | (a & cin);

endmodule
