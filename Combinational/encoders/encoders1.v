module case_encoder (
  input [DATA_WIDTH-1:0] data,
  output reg [ADDR_WIDTH-1:0] addr,
  output reg valid
);

  always @(*) begin
    case (data)
      {DATA_WIDTH-1'b0, 1'b1}: begin
        addr = 0;
        valid = 1;
      end
      {DATA_WIDTH-2'b0, 2'b11}: begin
        addr = 1;
        valid = 1;
      end
      // ... additional cases for other data values
      default: begin
        addr = 'bx;
        valid = 0; // Handle unknown cases
      end
    endcase
  end

endmodule
