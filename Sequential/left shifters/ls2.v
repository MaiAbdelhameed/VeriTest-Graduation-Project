module left_shift_register_enable (
  input d,
  input clk,
  input enable,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    if (enable) begin
      q <= {d, q[N-2:0]}; // Shift left only when enabled
    end
  end

endmodule
