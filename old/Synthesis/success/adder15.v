module adder15(input [1:0] A, B, input Cin, output reg [1:0] Sum, output reg Cout);

always @(*) begin
    Sum[0] = A[0] ^ B[0] ^ Cin;
    Sum[1] = A[1] ^ B[1] ^ ((A[0] & B[0]) | (Cin & (A[0] ^ B[0])));
    Cout = ((A[0] & B[0]) | (Cin & (A[0] ^ B[0]))) | ((A[1] & B[1]) | ((A[0] & B[0]) & (A[1] ^ B[1])));
end

endmodule
