module comparator5 (A,B,C,D,E);
    input A,B;
    output C,D,E;

and g1 (C,~A,B); // A<B
and g2 (E,~B,A); // A>B
nor g3 (D,C,E); // A=B

endmodule