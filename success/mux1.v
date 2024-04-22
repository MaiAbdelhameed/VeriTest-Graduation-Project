module mux1 ( // mux4x1
  input wire [7:0] A,
  input wire [7:0] B,
  input wire [7:0] C,
  input wire [7:0] D,
  input wire [1:0] Select,
  output [7:0] Y
);

reg [7:0] temp;

always @ (*)
begin
  case (Select)
    2'b00:
    temp = A;
    2'b01:
    temp = B;
    2'b10: 
    temp = C;
    2'b11:
    temp = D;
  endcase
end

assign Y = temp;

endmodule

