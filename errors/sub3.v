module sub3 (
  input A, 
  input B, 
  input Bin,  // Borrow-in
  output Difference, 
  output Bout  // Borrow-out
);
  xor x1 (Difference, A, B, Bin);
  and a1 (a, ~A, B, Bin);
  and a2 (b, ~A, ~B, Bin);
  and a3 (c, A, ~B, Bin);
  or o1 (Bout, a, b, c);
endmodule

Error occurred: 'NoneType' object has no attribute 'name'