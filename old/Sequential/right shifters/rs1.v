module right_shift_register (
  input d,
  input clk,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    q <= {q[N-2:0], d}; // Shift right on every clock edge
  end

endmodule
