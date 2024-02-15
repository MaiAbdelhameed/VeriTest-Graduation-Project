// modulo counter:This counter counts up to a certain value (modulo) before wrapping back to 0.
module modulo_counter (
  input clk,
  input rst,
  input [WIDTH-1:0] modulo,
  output reg [WIDTH-1:0] count
);

  always @(posedge clk) begin
    if (rst) begin
      count <= 0;
    end else begin
      if (count == modulo) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end

endmodule
