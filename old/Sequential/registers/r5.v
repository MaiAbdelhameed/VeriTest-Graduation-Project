module primitive_register #(parameter WIDTH = 8) (
  input [WIDTH-1:0] d,
  input clk,
  input reset,
  output reg [WIDTH-1:0] q
);

  // Use a specific registered type based on tool support (e.g., regsync #(N) from Xilinx)

endmodule
