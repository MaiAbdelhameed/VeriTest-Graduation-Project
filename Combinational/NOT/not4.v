module not4 (
  input in,
  output out
);

  case (in)
    1'b0: out = 1'b1;
    1'b1: out = 1'b0;
  endcase

endmodule