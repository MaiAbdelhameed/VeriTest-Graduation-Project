module table_encoder (
  input [DATA_WIDTH-1:0] data,
  output reg [ADDR_WIDTH-1:0] addr,
  output reg valid
);

  table
    input {data};
    output {valid, addr};
  begin
    {DATA_WIDTH'b0, 1'b0}: {1'b0, 'bx}; // All bits 0: invalid
    {DATA_WIDTH-1'b0, 1'b1}: {1'b1, 0}; // First bit high: encoded at 0
    // ... additional entries for other data combinations
  endtable

endmodule
