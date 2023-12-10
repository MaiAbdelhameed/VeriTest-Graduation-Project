module mux_4to1 (
 data_in, select, data_out
);

 input  [3:0] a,b;
  input  [1:0] select;
  output [3:0] data_out, data;

assign data_out =  a & b;
assign data = a & b;

endmodule
