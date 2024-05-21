
// tested
module adder10(A, B, Sum, Cin, Cout);

    input [1:0] A,B;
    output reg [1:0] Sum;
    input Cin;
    output reg Cout;

    always @(*) begin
        {Cout,Sum} = A + B + Cin;
    end

endmodule
