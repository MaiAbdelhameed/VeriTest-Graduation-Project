//built-in operator
module or21 (
  input [2:0] a,
  input [2:0] b,
  output [2:0] out
);

  assign out = {(a[2] | b[2]), (a[1] | b[1]), (a[0] | b[0])};

endmodule