module seven_segment_logic (
  input [3:0] digit,
  output reg [6:0] segments
);

  always_comb begin
    segments[0] = ~digit[0] & ~digit[1] & ~digit[3]; // Segment a
    segments[1] = ~digit[0] & digit[1] & ~digit[2]; // Segment b
    // ... conditions for other segments
  end

endmodule
