// up-down counter: This counter allows both incrementing and decrementing based on a control signal.
module up_down_counter (
  input clk,
  input rst,
  input up_down,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
    end else begin
      if (up_down) begin
        count <= count + 1;
      end else begin
        count <= count - 1;
      end
    end
  end

endmodule