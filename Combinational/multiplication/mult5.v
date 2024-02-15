module primitive_multiplier (
  input [A_WIDTH-1:0] a,
  input [B_WIDTH-1:0] b,
  output reg [OUT_WIDTH-1:0] out
);

  multiplier #(A_WIDTH, B_WIDTH, OUT_WIDTH) multiplier_inst (.a(a), .b(b), .out(out));

endmodule
