module pe27 (input [3:0] in, output reg [1:0] out);

    always @* begin
        out[0] = in[3] | in[1];
        out[1] = in[3] ? 1'b1 : in[2] ? 1'b0 : in[1] ? 1'b1 : in[0] ? 1'b0 : 1'b0;
    end

endmodule
