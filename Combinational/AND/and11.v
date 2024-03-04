module and11 (
  input a,
  input b,
  output out
);

  case ({a, b})
    2'b00: out = 1'b0;
    2'b01, 2'b10: out = 1'b0;
    default: out = 1'b1;
  endcase

endmodule