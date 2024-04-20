module pe_circuit7 (A0, A1, Y0, Y1, Y2, Y3);

input Y0, Y1, Y2, Y3;
output A0, A1;
wire Y2bar, W1;


    not U1(Y2bar, Y2);
    and U2(W1 ,Y2bar, Y1);
    or U3(A1, Y3, Y2);
    or U4(A0,Y1, W1);

endmodule