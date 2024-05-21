module decoder50 (input [2:0] in, output [7:0] out);

    reg [7:0] temp;
    always @(*) begin
        
        temp[0] = ~(in[0] & in[1] & in[2]);
        temp[1] = ~(in[0] & in[1] & ~in[2]);
        temp[2] = ~(in[0] & ~in[1] & in[2]);
        temp[3] = ~(in[0] & ~in[1] & ~in[2]);
        temp[4] = ~(~in[0] & in[1] & in[2]);
        temp[5] = ~(~in[0] & in[1] & ~in[2]);
        temp[6] = ~(~in[0] & ~in[1] & in[2]);
        temp[7] = ~(~in[0] & ~in[1] & ~in[2]);
    end 

    assign out = temp;
endmodule
