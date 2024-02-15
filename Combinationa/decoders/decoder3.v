module assign_decoder (
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  always @(*) begin
    out[0] = (addr == 0) ? 1'b1 : 1'b0;
    out[1] = (addr == 1) ? 1'b1 : 1'b0;
    // ... additional outputs based on address
  end

endmodule
d