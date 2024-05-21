//basic counter : This is a simple synchronous counter that increments on each clock edge and resets to 0 on an active-low reset signal.
module simple_counter (
  input clk,
  input rst,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
    end else begin
      count <= count + 1;
    end
  end

endmodule