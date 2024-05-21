module ring_counter (
  input clk,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    count[0] <= count[WIDTH-1];
    for (int i = 1; i < WIDTH; i++) begin
      count[i] <= count[i-1];
    end
  end

endmodule