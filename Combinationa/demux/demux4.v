module gate_level_demux (
  input in,
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  wire [OUT_WIDTH-1:0] not_addr;
  not #(ADDR_WIDTH) not_inst (not_addr, addr);

  and a1 [OUT_WIDTH-1:0] (out, in, not_addr);
  and a2 [OUT_WIDTH-1:0] (out, addr, in);

endmodule
