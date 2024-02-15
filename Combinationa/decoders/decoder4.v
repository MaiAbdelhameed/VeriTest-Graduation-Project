module gate_level_decoder (
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  wire [ADDR_WIDTH-1:0] not_addr;
  not #(ADDR_WIDTH) not_inst (not_addr, addr);

  and a1 [OUT_WIDTH-1:0] (out, 1'b1, not_addr);
  and a2 [OUT_WIDTH-1:0] (out, addr, 1'b0);

endmodule
