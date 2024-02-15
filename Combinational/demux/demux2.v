module primitive_demux (
  input in,
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  always @(*) begin
    decoder #(OUT_WIDTH, ADDR_WIDTH) decoder_inst (out, in, addr);
  end

endmodule