module shift_register (
  input d,
  input clk,
  input shift_in,
  output shift_out,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    if (shift_in) begin
      q <= {d, q[N-2:0]}; // Shift left or right based on logic
    end else begin
      q <= q;
    end
  end

  assign shift_out = q[0]; // Assign output from last bit

endmodule
