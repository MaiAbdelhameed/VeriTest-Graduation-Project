module repeated_subtraction_divider (
  input [DATA_WIDTH-1:0] dividend,
  input [DATA_WIDTH-1:0] divisor,
  output reg [DATA_WIDTH-1:0] quotient,
  output reg [DATA_WIDTH-1:0] remainder
);

  reg [DATA_WIDTH-1:0] current_dividend;
  integer i;

  always @(*) begin
    current_dividend = dividend;
    quotient = 0;
    for (i = 0; i < DATA_WIDTH; i++) begin
      if (current_dividend >= divisor) begin
        current_dividend = current_dividend - divisor;
        quotient = quotient + 1;
      end
    end
    remainder = current_dividend;
  end

endmodule
