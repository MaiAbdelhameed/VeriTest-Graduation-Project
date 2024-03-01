module pe7(A0, A1, Y0, Y1, Y2, Y3);
input Y0, Y1, Y2, Y3;
output A0, A1;
wire Y2bar;
not U1(.F(Y2bar), . e(Y2) ) ;
and U2(.Z(W1) ,. X(Y2bar), . Y(Y1)) ;
or (.C(A1), . A(Y3), . B(Y2)) ;
or(.C(A0),. A(Y1),. B(W1)) ;
endmodule;