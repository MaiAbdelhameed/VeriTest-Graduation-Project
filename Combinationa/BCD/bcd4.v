module bcd_display (
  input [3:0] bcd,
  output reg [6:0] segments
);

  always_comb begin
    // Use a case statement or LUT to map BCD digit to segment pattern
    case (bcd)
      4'd0: segments = 7'b1111110;
      // ... patterns for other digits
    endcase
  end

endmodule
