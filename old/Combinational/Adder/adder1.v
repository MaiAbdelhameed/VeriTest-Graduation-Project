module adder1 (
  input A, 
  input B, 
  input Cin, 
  output Sum, 
  output Cout
);
  xor x1 (Sum, A, B, Cin);
  and a1 (a, A, B);
  and a2 (b, A, Cin);
  and a3 (c, B, Cin);
  or o1 (Cout, a, b, c);
endmodule