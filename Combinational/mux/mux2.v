// case statement mux
module case_mux (
  input [WIDTH-1:0] in0,
  input [WIDTH-1:0] in1,
  input sel,
  output reg [WIDTH-1:0] out
);

  always @(*) begin
    case (sel)
      0: out = in0;
      1: out = in1;
      default: out = 'bx; // Handle unknown cases
    endcase
  end

endmodule