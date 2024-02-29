module case_and (
  input a,
  input b,
  output out
);

  case ({a, b})
    2'b00: out = 1'b0;
    2'b01, 2'b10: out = 1'b0;
    2'b11: out = 1'b1;
    default: out = 1'bx; // handle unknown cases
  endcase

endmodule