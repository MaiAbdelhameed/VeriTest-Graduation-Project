// Gray code counter: This counter uses a special encoding to minimize glitches during transitions between states.
module gray_counter (
  input clk,
  input rst,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
    end else begin
      count[0] <= ~count[0];
      for (int i = 1; i < WIDTH; i++) begin
        count[i] <= count[i-1] ^ count[i];
      end
    end
  end

endmodule