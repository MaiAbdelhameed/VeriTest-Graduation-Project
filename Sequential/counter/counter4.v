// ripple counter: This counter uses individual flip-flops connected in a chain, where each flip-flop toggles on the rising edge of its previous stage's output.
module ripple_counter (
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
        if (count[i-1] == 1) begin
          count[i] <= ~count[i];
        end else begin
          count[i] <= count[i];
        end
      end
    end
  end

endmodule
