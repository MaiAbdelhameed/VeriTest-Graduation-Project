module adder16(input A0,A1, B0,B1, input Cin, output reg [1:0] Sum, output reg Cout);

always @(*) begin
    Sum[0] = A0 ^ B0 ^ Cin;
    Sum[1] = A1 ^ B1 ^ ((A0 & B0) | (Cin & (A0 ^ B0)));
    Cout = ((A0 & B0) | (Cin & (A0 ^ B0))) | ((A1 & B1) | ((A0 & B0) & (A1 ^ B1)));
end

endmodule
