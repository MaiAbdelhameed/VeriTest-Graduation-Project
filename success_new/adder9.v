// tested
module adder9(A0,A1,B0, B1, Sum, Cin, Cout);

    input A0,A1,B0,B1;
    output [1:0] Sum;
    input Cin;
    output Cout;

assign {Cout,Sum} = {A1,A0} + {B1,B0} + Cin;

endmodule
