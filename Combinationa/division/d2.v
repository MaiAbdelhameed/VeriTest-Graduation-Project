module restoring_divider (
  input [DATA_WIDTH-1:0] dividend,
  input [DATA_WIDTH-1:0] divisor,
  output reg [DATA_WIDTH-1:0] quotient,
  output reg [DATA_WIDTH-1:0] remainder
);

  reg [2*DATA_WIDTH-1:0] partial_remainder;
  integer i;

  always @(*) begin
    partial_remainder = dividend << DATA_WIDTH; // Left-shift dividend
    quotient = 0;
    for (i = 0; i < DATA_WIDTH; i++) begin
      if (partial_remainder >= 0) begin
        partial_remainder = partial_remainder - divisor;
        quotient = quotient | (1 << i); // Set quotient bit
      end else begin
        partial_remainder = partial_remainder + divisor;
      end
      partial_remainder = partial_remainder << 1; // Shift partial remainder
    end
    remainder = partial_remainder >> DATA_WIDTH; // Extract remainder
  end

endmodule
