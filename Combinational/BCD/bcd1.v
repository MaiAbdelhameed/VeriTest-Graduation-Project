module binary_to_bcd (
  input [15:0] binary,
  output reg [3:0] bcd0,
  output reg [3:0] bcd1,
  output reg [3:0] bcd2,
  output reg [3:0] bcd3
);

  always_ff @(posedge clk) begin
    bcd3 = binary[15:12];
    bcd2 = (binary[11:8] + bcd3) & 4'b1111;
    bcd1 = (binary[7:4] + bcd2) & 4'b1111;
    bcd0 = (binary[3:0] + bcd1) & 4'b1111;
  end

endmodule
