module bcd_adder (
  input [3:0] a,
  input [3:0] b,
  output reg [3:0] sum,
  output reg overflow
);

  always_ff @(posedge clk) begin
    {overflow, sum} = a + b;
    if (sum > 9) begin
      sum = sum + 6; // BCD correction
      overflow = 1;
    end
  end

endmodule
