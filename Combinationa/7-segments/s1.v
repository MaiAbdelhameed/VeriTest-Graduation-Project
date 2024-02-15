module seven_segment_direct (
  input [3:0] digit,
  output reg [6:0] segments
);

  always_comb begin
    case (digit)
      4'd0: segments = 7'b1111110; // Pattern for 0
      4'd1: segments = 7'b0110000; // Pattern for 1
      // ... patterns for other digits
    endcase
  end

endmodule
