module IfElseExample (
  input[2:0] a,
  input[2:0] b,
  output [5:0] result
);


  assign result[2:0] = a & b;
  assign result [5:3] = a ^ b;

  
endmodule
