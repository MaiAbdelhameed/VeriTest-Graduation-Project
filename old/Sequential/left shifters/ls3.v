module left_shift_register_load (
  input [N-1:0] d,
  input clk,
  input load,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    if (load) begin
      q <= d; // Load new data directly
    end else begin
      q <= {d, q[N-2:0]}; // Shift left otherwise
    end
  end

endmodule
