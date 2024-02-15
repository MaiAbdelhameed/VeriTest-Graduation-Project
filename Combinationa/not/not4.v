module case_not (
  input in,
  output out
);

  case (in)
    1'b0: out = 1'b1;
    1'b1: out = 1'b0;
    default: out = 1'bx; // Handle unknown cases
  endcase

endmodule