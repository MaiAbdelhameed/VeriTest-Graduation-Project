module seven_segment_direct (
  input [3:0] digit,
  output reg [6:0] segments
);

  always_comb begin
    case (digit)
      4'd0: segments = 7'b1111110; // Pattern for 0
      4'd1: segments = 7'b0110000; // Pattern for 1
      4'd2: segments = 7'b1011011; // Pattern for 2
      4'd3: segments = 7'b1001100; // Pattern for 3
      4'd4: segments = 7'b0110011; // Pattern for 4
      4'd5: segments = 7'b1001101; // Pattern for 5
      4'd6: segments = 7'b1011110; // Pattern for 6
      4'd7: segments = 7'b0110001; // Pattern for 7
      4'd8: segments = 7'b1111111; // Pattern for 8
      4'd9: segments = 7'b1001111; // Pattern for 9
      default: segments = 7'b0000000; // Pattern for invalid input
    endcase
  end

endmodule