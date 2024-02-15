module gate_full_adder (
  input a,
  input b,
  input cin,
  output sum,
  output cout
);

  xor xor1 (sum_xor, a, b);
  xor xor2 (sum, sum_xor, cin);
  and and1 (cout1, a, b);
  and and2 (cout2, b, cin);
  and and3 (cout3, a, cin);
  or or_gate (cout, cout1, cout2, cout3);

endmodule
