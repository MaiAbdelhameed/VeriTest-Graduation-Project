module decoder24 (din, en, dout);
  input [1:0] din; //2bit input
  input en; //enable
  output [3:0] dout;  //4bit output

  //a=din[0], b=din[1]
  //output assignments
  assign dout[0] = (~din[0]) & (~din[1]) & en;  //~a&~b&en
  assign dout[1] = (~din[0]) & (din[1]) & en; //~a&b&en
  assign dout[2] = (din[0]) & (~din[1]) & en; //a&~b&en
  assign dout[3] = (din[0]) & (din[1]) & en;  //a&b&en

endmodule