module encoder27 (input [1:0] in, output reg out);

    always @(*) begin
        if (in[1]) begin
            out = 2'b10;
        end else if (in[0]) begin
            out = 2'b01;
        end else begin
            out = 2'b00;
        end
    end
    

endmodule
