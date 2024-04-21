module decoder40 (input [1:0] in, output reg [3:0] out);


    always @(*) begin
        out[0] = ~in[0] & ~in[1];
        out[1] = ~in[0] & in[1];
        out[2] = in[0] & ~in[1];
        out[3] = in[0] & in[1];
        
    end

endmodule
