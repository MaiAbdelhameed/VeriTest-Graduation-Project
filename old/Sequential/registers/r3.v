module parameterized_register #(parameter WIDTH = 8) (
  input [WIDTH-1:0] d,
  input clk,
  output reg [WIDTH-1:0] q
);

  always_ff @(posedge clk) begin
    q <= d;
  end

endmodule
