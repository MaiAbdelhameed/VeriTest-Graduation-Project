module gray_carry_counter (
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
        count[i] <= count[i-1] ^ count[i]^count[0]; // XOR with carry and initial bit
      end
    end
  end

endmodule