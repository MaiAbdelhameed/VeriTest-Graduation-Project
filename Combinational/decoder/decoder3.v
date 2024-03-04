module decoder3 (en,a,b,y);
    // declare input and output ports
    input en,a,b;
    output [3:0]y;

    // supportive connection required
    wire enb,na,nb;
    assign enb = ~en;
    assign na = ~a;
    assign nb = ~b;
    
    // assign output value by referring to logic diagram
    assign y[0] = ~(enb&na&nb);
    assign y[1] = ~(enb&na&b);
    assign y[2] = ~(enb&a&nb);
    assign y[3] = ~(enb&a&b);

endmodule