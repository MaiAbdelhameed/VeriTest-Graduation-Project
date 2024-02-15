module piso_right_shift_register (
  input [N-1:0] d,
  input clk,
  output reg q_out
);

  integer i;

  always_ff @(posedge clk) begin
    q_out <= q[N-1]; // Output most significant bit
    for (i = N-1; i >= 1; i = i-1) begin
      q[i] <= q[i-1]; // Shift right
    end
    q[0] <= d[0]; // Serial input
  end

endmodule
