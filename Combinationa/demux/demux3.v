module assign_demux (
  input in,
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  always @(*) begin
    out[0] = (addr == 0) ? in : 1'b0;
    out[1] = (addr == 1) ? in : 1'b0;
    // ... additional outputs based on address
  end

endmodule
