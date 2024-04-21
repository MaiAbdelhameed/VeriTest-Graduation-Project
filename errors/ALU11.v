module ALU11 (op,a,b,opcode);

  output reg [7:0] op;     //output of alu
   input [7:0]     a,b;    //inputs to alu
   input [3:0] opcode;     //control signal for different operation

always @(*)
begin
    case (opcode)
        4'b0000 : op = a + b;
        4'b0001 : op = a - b;
        4'b0010 : op = a * b; 
        4'b0011 : op = a / b;
        4'b0100 : op = a % b;
        4'b0101 : op = a & b; 
        4'b0110 : op = a | b;
        4'b0111 : op = a && b;
        4'b1000 : op = a || b; 
        4'b1001 : op = a ^ b;
        4'b1010 : op = ~ a;
        4'b1011 : op = ! a; 
        4'b1100 : op = a >> 1; 
        4'b1101 : op = a << 1 ; 
        4'b1110 : op = a + 1; 
        4'b1111 : op = a - 1; 
    endcase

end
endmodule
Error occurred: 'Divide' object has no attribute 'name'