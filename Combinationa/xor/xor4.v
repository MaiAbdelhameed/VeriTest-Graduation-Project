module case_xor (
  input a,
  input b,
  output out
);

  case ({a, b})
    2'b00, 2'b11: out = 1'b0; // Both bits same
    2'b01, 2'b10: out = 1'b1; // Bits different
    default: out = 1'bx; // Handle unknown cases
  endcase

endmodule