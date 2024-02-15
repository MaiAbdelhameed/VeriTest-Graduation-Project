module array_multiplier (
  input [3:0] a,
  input [3:0] b,
  output reg [7:0] out
);

  // Generate partial products
  reg [3:0] pp [3:0];
  integer i, j;

  always_comb begin
    for (i = 0; i < 4; i = i + 1) begin
      for (j = 0; j < 4; j = j + 1) begin
        pp[i][j] = a[i] * b[j];
      end
    end
  end

  // Shift and accumulate partial products
  reg [7:0] accum = 0;
  for (i = 0; i < 4; i = i + 1) begin
    for (j = 0; j < 4; j = j + 1) begin
      accum = accum + (pp[i][j] << i*j);
    end
  end

  out = accum;

endmodule
