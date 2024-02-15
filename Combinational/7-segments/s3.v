module seven_segment_decoder (
  input [3:0] digit,
  output reg [6:0] segments
);

  always_comb begin
    case (digit)
      4'd0: segments = 4'b0001; // Activate segment a
      4'd1: segments = 4'b1000; // Activate segment b
      // ... decoder outputs for other segments
    endcase
  end

endmodule
