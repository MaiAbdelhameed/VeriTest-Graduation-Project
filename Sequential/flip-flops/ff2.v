module d_flip_flop_always_posedge (
  input d,
  input clk,
  output reg q
);

  always @(posedge clk) begin
    q <= d;
  end

endmodule
