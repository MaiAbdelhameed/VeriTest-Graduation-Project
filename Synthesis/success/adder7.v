module adder7(A, B, Sum, Cin, Cout);

    input [3:0] A,B;
    output [3:0] Sum;
    input Cin;
    output Cout;

assign {Cout,Sum} = A + B + Cin;

endmodule
