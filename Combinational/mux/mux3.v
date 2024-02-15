//primitivate mux
module primitive_mux (
  input [WIDTH-1:0] in0,
  input [WIDTH-1:0] in1,
  input sel,
  output reg [WIDTH-1:0] out
);

  always @(*) begin
    mux #(WIDTH) mux_inst (out, in0, in1, sel);
  end

endmodule