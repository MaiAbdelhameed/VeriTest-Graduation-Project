module jfulladder(output[2:0] y, output[2:0] carryout, input a, input b,input carryin);

  
  assign y = a ^ b ^ carryin;
 
  
endmodule