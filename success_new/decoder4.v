module decoder4 (en,a,b,y);
    // declare input and output ports
    input en,a,b;
    output [3:0]y;

    // supportive connections required
    // to connect nand gates
    wire enb,na,nb;

    // instantiate 4 nand gates and 3 not gates
    // make connections by referring the above logic diagram
    not n0(enb,en);
    not n1(na,a);
    not n2(nb,b);

    nand n3(y[0],enb,na,nb);
    nand n4(y[1],enb,na,b);
    nand n5(y[2],enb,a,nb);
    nand n6(y[3],enb,a,b);

endmodule