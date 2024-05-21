module decoder49 (input [2:0] in, output reg [7:0] out);

    always @(*) begin
        
        out[0] = ~(in[0] & in[1] & in[2]);
        out[1] = ~(in[0] & in[1] & ~in[2]);
        out[2] = ~(in[0] & ~in[1] & in[2]);
        out[3] = ~(in[0] & ~in[1] & ~in[2]);
        out[4] = ~(~in[0] & in[1] & in[2]);
        out[5] = ~(~in[0] & in[1] & ~in[2]);
        out[6] = ~(~in[0] & ~in[1] & in[2]);
        out[7] = ~(~in[0] & ~in[1] & ~in[2]);
    end 
endmodule
