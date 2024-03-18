module adder18(input A0,A1,A2, B0,B1,B2, input Cin, output reg [2:0] Sum, output reg Cout);

always @* begin
    Sum[0] = A0 ^ B0 ^ Cin;
    Sum[1] = A1 ^ B1 ^ ((A0 & B0) | (Cin & (A0 ^ B0)));
    Sum[2] = A2 ^ B2 ^ ((A1 & B1) | ((A0 & B0) & (A1 ^ B1)) | (Cin & ((A0 & B0) | (A1 & B1))));
    Cout = ((A0 & B0) | (Cin & (A0 ^ B0))) | ((A1 & B1) | ((A0 & B0) & (A1 ^ B1))) | ((A2 & B2) | ((A1 & B1) & ((A0 & B0) | (A1 & B1))));
end

endmodule
