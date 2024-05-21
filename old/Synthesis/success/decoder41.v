module decoder41 (input [1:0] in, output [3:0] out);


    reg [3:0] temp;

    always @(*) begin
        temp[0] = ~in[0] & ~in[1];
        temp[1] = ~in[0] & in[1];
        temp[2] = in[0] & ~in[1];
        temp[3] = in[0] & in[1];
        
    end

    assign out = temp;
    
endmodule