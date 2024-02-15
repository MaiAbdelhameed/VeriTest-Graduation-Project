module seven_segment_primitive (
  input [3:0] digit,
  output reg [6:0] segments
);

  seven_segment_display #(.COMMON_ANODE(0)) seg_inst (.digit(digit), .segments(segments));

endmodule
