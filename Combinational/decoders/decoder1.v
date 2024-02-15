module case_decoder (
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  always @(*) begin
    case (addr)
      0: out = {OUT_WIDTH{1'b1}}; // All outputs high for specific address
      1: out = {OUT_WIDTH-1'b0, 1'b1}; // Set only second output high
      // ... additional cases for other addresses
      default: out = 'bx; // Handle unknown cases
    endcase
  end

endmodule
