// Synchronous counter with counter enable: This counter only increments when a separate "enable" signal is active.
module counter_with_enable (
  input clk,
  input rst,
  input enable,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
    end else if (enable) begin
      count <= count + 1;
    end
  end

endmodule