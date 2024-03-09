module encoder50 (input [3:0] in, output reg [1:0] out);

    always @(*) begin
        out[0] = in[3] | in[1];
        out[1] = in[3] | in[2];
    end


endmodule
