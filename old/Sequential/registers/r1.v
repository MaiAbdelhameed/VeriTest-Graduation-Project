module single_bit_register (
  input d,
  input clk,
  output reg q
);

  always_ff @(posedge clk) begin
    q <= d;
  end

endmodule