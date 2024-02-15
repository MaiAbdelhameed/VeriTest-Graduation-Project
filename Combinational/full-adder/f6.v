module primitive_full_adder (
  input a,
  input b,
  input cin,
  output sum,
  output cout
);

  full_adder #(1) primitive_adder (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

endmodule
