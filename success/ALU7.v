module ALU7 (
  input  [7:0] A,
  input  [7:0] B,
  input  [3:0] op,
  output reg [7:0] out
);

  always@(*) begin
    case (op)
      4'b0000: out = A + B;
      4'b0001: out = A - B;
      4'b0010: out = A << B;
      4'b0011: out = A >>> B;
      4'b0100: out = A >> B;
      4'b0101: out = A & B;
      4'b0110: out = A | B;
      4'b0111: out = A ^ B;
      4'b1000: out = (A == B) ? 1'b1 : 1'b0;
      default:         out = 8'b0;
    endcase
  end

endmodule