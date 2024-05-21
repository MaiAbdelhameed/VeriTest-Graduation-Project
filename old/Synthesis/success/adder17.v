module adder17(input [2:0] A, B, input Cin, output reg [2:0] Sum, output reg Cout);

always @* begin
    Sum[0] = A[0] ^ B[0] ^ Cin;
    Sum[1] = A[1] ^ B[1] ^ ((A[0] & B[0]) | (Cin & (A[0] ^ B[0])));
    Sum[2] = A[2] ^ B[2] ^ ((A[1] & B[1]) | ((A[0] & B[0]) & (A[1] ^ B[1])) | (Cin & ((A[0] & B[0]) | (A[1] & B[1]))));
    Cout = ((A[0] & B[0]) | (Cin & (A[0] ^ B[0]))) | ((A[1] & B[1]) | ((A[0] & B[0]) & (A[1] ^ B[1]))) | ((A[2] & B[2]) | ((A[1] & B[1]) & ((A[0] & B[0]) | (A[1] & B[1]))));
end

endmodule
