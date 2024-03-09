module encoder28 (input [1:0] in, output reg out);

    always @(*) begin
        out = (in[1]) ? 2'b10 : (in[0]) ? 2'b01 : 2'b00;
    end

endmodule
