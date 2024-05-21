module n_bit_register (
  input [N-1:0] d,
  input clk,
  output reg [N-1:0] q
);

  always_ff @(posedge clk) begin
    q <= d;
  end

endmodule
