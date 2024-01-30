module IfExample(
  input wire [3:0] data_input,
  input[2:0] clk, rst,
  output[5:0] fin
  
);


assign fin = data_input[1] ? clk & clk : rst & clk;
endmodule
