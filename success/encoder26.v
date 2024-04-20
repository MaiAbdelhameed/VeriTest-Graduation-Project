//2x1
module encoder26 (input [1:0] in, output out);

    assign out = (in[1]) ? 2'b10 : (in[0]) ? 2'b01 : 2'b00;

endmodule
