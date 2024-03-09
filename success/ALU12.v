module ALU12(input [3:0] aluin_a, aluin_b, OPCODE, input Cin, output reg [3:0] alu_out, output reg Cout, output reg OF);

always@(*) begin
case (OPCODE)
// add
4'b1000 : begin
{Cout,alu_out} = aluin_a+aluin_b;
end
// add with Cin
4'b1001 : begin
{Cout,alu_out} = aluin_a+aluin_b+Cin;
end
// sub a from b
4'b1010 : begin
{Cout,alu_out} = aluin_a-aluin_b;
end
// bitwise NAND
4'b0000 : begin
alu_out = ~(aluin_a & aluin_b);
Cout = 1'b0;
end
// bitwise NOR
4'b0001 : begin
alu_out = ~(aluin_a | aluin_b);
Cout = 1'b0;
end
// bitwise XOR
4'b0010 : begin
alu_out = aluin_a^aluin_b;
Cout = 1'b0;
end
// bitwise inversion
4'b0100 : begin
alu_out = ~aluin_a;
Cout = 1'b0;
end
// logical left shift
4'b0101 : begin
alu_out = aluin_a << aluin_b;
Cout = 1'b0;
end
default : begin
alu_out = 0; Cout = 0;
end
endcase
end
endmodule