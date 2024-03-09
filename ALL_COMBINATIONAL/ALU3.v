module ALU3 (A,B,out, operation);
input [31:0] A,B;
input [2:0] operation;
output reg [63:0] out;

    always@(*) begin
        case (operation)
            3'b000: out = A+B;
            3'b001: out = A-B;
            3'b010: out = A*B;
            3'b011: out = A/B;
            3'b100: out = A&B;
            3'b101: out = A|B;
            3'b110: out = A^B;
            3'b111: out = ~(A^B);
        endcase
    end
endmodule