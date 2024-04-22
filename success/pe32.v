module pe32 (input [3:0] in, output [1:0] out);

    wire w1,w2,w3;
    
    assign w1 = in[1] & ~in[2];
    assign w2 = w1 | in[3];
    
    assign out[0] = w2;
    assign out[1] = in[2] | in[3];

endmodule
