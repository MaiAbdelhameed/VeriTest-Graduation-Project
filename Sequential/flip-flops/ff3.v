module d_flip_flop_reg_delay (
  input d,
  input clk,
  output reg q
);

  always @(posedge clk) begin
    #1 q = d; // Delay of 1 unit for flip-flop behavior
  end

endmodule
