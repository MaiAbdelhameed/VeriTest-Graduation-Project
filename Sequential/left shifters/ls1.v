module left_shift_register (
  input d,
  input clk,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    q <= {d, q[N-2:0]}; // Shift left on every clock edge
  end

endmodule
