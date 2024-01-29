module IfExample(
  input wire [3:0] data_input,
  input[2:0] clk, rst
  
);
  wire [2:0] result, result2;
  assign result[1:0] = (data_input[1] >= 1'b0) ? {clk[0], rst[1]} : data_input[2];
  assign result[2] = data_input[2];
 

endmodule