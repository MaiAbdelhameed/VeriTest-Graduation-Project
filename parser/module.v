module half_adder(a, b, s, cout);
  input [3:0] a,b,c,d;
  wire [3:0] k;
  output  [3:0] s;
  assign k = c | b;
  assign s = k & a;




  

endmodule