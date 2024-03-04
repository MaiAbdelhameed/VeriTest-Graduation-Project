//case statements
module or5 (
  input a,
  input b,
  output out
);

  case ({a, b})
    2'b00: out = 1'b0;
    2'b01, 2'b10, 2'b11: out = 1'b1;
    default: out = 1'bx;
  endcase

endmodule