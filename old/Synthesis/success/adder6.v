module adder6(A,B,Cin,Sum,Cout);
    input A,B,Cin;
    output Sum,Cout;

    wire w1,w2,w3;

    xor x1 (w1,A,B);
    and A1 (w2,w1,Cin);
    xor X2 (Sum,w1,Cin);
    and A2 (w3,A,B);
    or O1 (Cout,w3,w2);
    
endmodule