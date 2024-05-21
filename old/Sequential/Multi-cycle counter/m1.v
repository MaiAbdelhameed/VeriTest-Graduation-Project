module multi_cycle_counter (
  input clk,
  input rst,
  output reg [WIDTH-1:0] count
);

  parameter CYCLE_COUNT = 4; // Count up every 4 clock cycles

  reg [CYCLE_COUNT-1:0] cycle_counter;

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
      cycle_counter <= 0;
    end else begin
      if (cycle_counter == CYCLE_COUNT-1) begin
        count <= count + 1;
        cycle_counter <= 0;
      end else begin
        cycle_counter <= cycle_counter + 1;
      end
    end
  end

endmodule