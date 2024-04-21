module comparator4 (A,B,C,D,E);
    input A,B;
    output C,D,E;

wire not_A,not_B,or_out;

not n1 (not_A,A);
and g1 (C,not_A,B); // A<B
not n2 (not_B,B);
and g2 (E,not_B,A); // A>B
or g3 (or_out,C,E);
not g4 (D,or_out); // A=B

endmodule