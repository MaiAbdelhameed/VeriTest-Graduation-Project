module johnson_counter (
  input clk,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    count[0] <= count[WIDTH-1];
    count[WIDTH-1] <= count[WIDTH-2] ^ count[0];
    for (int i = 1; i < WIDTH-1; i++) begin
      count[i] <= count[i-1];
    end
  end

endmodule