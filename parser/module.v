module IfExample(
  input wire [3:0] data_input,
  input clk, rst,
  output reg result
);

  always @(posedge clk or posedge rst) begin
    if (rst) begin
      // Reset condition
      result <= 1'b0;
    end else begin
      // Regular condition
      if (data_input == 4'b1010) begin
        result <= 1'b1;
      end else begin
        result <= 1'b0;
      end
    end
  end

endmodule
