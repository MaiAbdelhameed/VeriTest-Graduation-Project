// tested
module mux1 ( // mux4x1
  input wire [7:0] A,
  input wire [7:0] B,
  input wire [7:0] C,
  input wire [7:0] D,
  input wire [1:0] Select,
  output reg [7:0] Y
);


always @ (*)
begin
  case (Select)
    2'b00:
    Y = A;
    2'b01:
    Y = B;
    2'b10: 
    Y = C;
    2'b11:
    Y = D;
  endcase
end


endmodule

