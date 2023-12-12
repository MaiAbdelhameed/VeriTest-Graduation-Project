module IfElseExample (
  input[2:0] a,
  input[2:0] b,
  output [1:0] result
);


  assign result[0] = a[0] & b[0];
  assign result[1] = a[0] ^ b[0];
 
  
endmodule
