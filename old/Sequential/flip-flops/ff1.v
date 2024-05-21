module d_flip_flop_always_ff (
  input d,
  input clk,
  output reg q
);

  always_ff @(posedge clk) begin
    q <= d;
  end

endmodule
