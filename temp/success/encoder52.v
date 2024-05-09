module encoder52 (input [3:0] in, output [1:0] out);

    wire w1,w2;

    or or1(w1,in[3],in[1]);
    or or2(w2, in[3],in[2]);

    assign out[0] = w1;
    assign out[1] = w2;


endmodule
