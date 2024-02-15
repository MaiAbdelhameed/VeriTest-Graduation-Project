module loop_priority_encoder (
  input [DATA_WIDTH-1:0] data,
  output reg [ADDR_WIDTH-1:0] addr,
  output reg valid
);

  always @(*) begin
    valid = 0;
    addr = 'bx;
    for (int i = 0; i < DATA_WIDTH; i++) begin
      if (data[i] == 1'b1) begin
        addr = i;
        valid = 1;
      end
    end
  end

endmodule
