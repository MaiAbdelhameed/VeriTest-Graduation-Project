module sipo_left_shift_register (
  input d,
  input clk,
  output reg [N-1:0] q
);

  integer i;

  always_ff @(posedge clk) begin
    for (i = N-1; i >= 1; i = i-1) begin
      q[i] <= q[i-1]; // Shift left
    end
    q[0] <= d; // Serial input
  end

endmodule
