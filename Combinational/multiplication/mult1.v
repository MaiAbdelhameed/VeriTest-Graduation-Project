module simple_multiplier (
  input [A_WIDTH-1:0] a,
  input [B_WIDTH-1:0] b,
  output reg [OUT_WIDTH-1:0] out
);

  assign out = a * b; // Use built-in multiplier

endmodule
