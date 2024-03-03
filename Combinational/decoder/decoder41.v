module decoder41(input [1:0] in, output reg [3:0] out);


    reg [3:0] temp;

    always @(*) begin
        assign temp[0] = ~in[0] & ~in[1];
        assign temp[1] = ~in[0] & in[1];
        assign temp[2] = in[0] & ~in[1];
        assign temp[3] = in[0] & in[1];
        
    end

    assign out = temp;
    
endmodule
