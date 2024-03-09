
////// check /////
module encoder30 (input [1:0] in, output [1:0] out);

    assign out[0] = in[1] | in[0];
    assign out[1] = in[1] ? 1'b0 : in[0] ? 1'b1 : 1'b0;

endmodule
