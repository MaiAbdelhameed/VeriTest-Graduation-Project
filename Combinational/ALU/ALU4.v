module ALU4(
input [2:0]opcode,
input [7:0]OperandA,OperandB,
output reg [7:0]result
    );
    
always @(*)begin
case(instruction)
3'b000:
    result = OperandA + B;
3'b001:
    result = OperandA - B;
3'b010:
    result = OperandA / B;
3'b011:
    result = OperandA * B;  
3'b100:
    result = OperandA & B; 
3'b101:
    result = OperandA | B;
3'b110:
    result = ~OperandA;
3'b111:
    result = OperandA ^ OperandA;
default:
    result = 0;
    endcase
end

endmodule