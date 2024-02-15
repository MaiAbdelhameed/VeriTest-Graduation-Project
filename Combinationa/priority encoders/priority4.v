module primitive_priority_encoder (
  input [DATA_WIDTH-1:0] data,
  output reg [ADDR_WIDTH-1:0] addr,
  output reg valid
);

  always @(*) begin
    priority_encoder #(DATA_WIDTH, ADDR_WIDTH) priority_inst (.data(data), .addr(addr), .valid(valid));
  end

endmodule
