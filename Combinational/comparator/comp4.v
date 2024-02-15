module gate_level_comparator (
  input [WIDTH-1:0] a,
  input [WIDTH-1:0] b,
  output reg eq,
  output reg greater,
  output reg less
);

  // ... implement logic using XOR, AND, OR gates for each bit comparison
  always @(*) begin
    // Combine gate outputs to determine eq, greater, and less
  end

endmodule