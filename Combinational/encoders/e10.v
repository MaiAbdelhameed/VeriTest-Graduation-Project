///4x2
module encoder4x2_basic_structural(input [3:0] in, output [1:0] out);

    assign out = (in[3]) ? 2'b11 : (in[2]) ? 2'b10 : (in[1]) ? 2'b01 : (in[0]) ? 2'b00 : 2'b00;

endmodule
