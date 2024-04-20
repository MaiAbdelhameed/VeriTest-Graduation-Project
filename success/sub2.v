module sub2 (a,b,c,D,cout);
input a,b ;
input c;
output D ;
output cout ;
wire w1,w2,w3;

xor g1(w1,b,a) ;
and g2(w2,~w1,c) ;
xor g3(D,c,w1) ;
and g4(w3,b,~a) ;
or g5(cout,w3,w2) ;

endmodule