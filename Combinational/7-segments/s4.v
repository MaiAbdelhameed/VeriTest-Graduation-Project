module seven_segment_lut (
  input [3:0] digit,
  output reg [6:0] segments
);

  reg [6:0] segment_patterns [0:9];

  initial begin
    segment_patterns[0] = 7'b1111110; // Pattern for 0
    segment_patterns[1] = 7'b0110000; // Pattern for 1
    // ... patterns for other digits
  end

  always_comb begin
    segments = segment_patterns[digit];
  end

endmodule
