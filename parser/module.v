module Example4 (
  input wire [3:0] a,
  output wire [1:0] y
);

  assign y = (a[3]) ? 2'b11 :
            (a[2]) ? 2'b10 :
            (a[1]) ? 2'b01 :
                     2'b00;

endmodule
