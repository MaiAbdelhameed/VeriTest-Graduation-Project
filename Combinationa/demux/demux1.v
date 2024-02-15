module case_demux (
  input in,
  input [ADDR_WIDTH-1:0] addr,
  output reg [OUT_WIDTH-1:0] out
);

  always @(*) begin
    case (addr)
      0: out = in ? 1'b1 : 1'b0;
      1: out = in ? 1'b0 : 1'b1;
      default: out = 1'bx; // Handle unknown cases
    endcase
  end

endmodule