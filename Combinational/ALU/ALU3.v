module ALU3 (A,B,out, operation);
input [31:0] A,B;
input [2:0] operation;
output reg [63:0] out;

    always@(*) begin
        case (operation)
            3'b000: Out = A+B;
            3'b001: Out = A-B;
            3'b010: Out = A*B;
            3'b011: Out = A/B;
            3'b100: Out = A&B;
            3'b101: Out = A|B;
            3'b110: Out = A^B;
            3'b111: Out = ~(A^B);
        endcase
    end
endmodule