module bcd_to_binary (
  input [3:0] bcd0,
  input [3:0] bcd1,
  input [3:0] bcd2,
  input [3:0] bcd3,
  output reg [15:0] binary
);

  always_ff @(posedge clk) begin
    binary = bcd3 * 10'd1000 + bcd2 * 10'd100 + bcd1 * 10'd10 + bcd0;
  end

endmodule
