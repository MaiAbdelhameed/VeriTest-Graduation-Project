module encoder51 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;
    always @(*) begin
        temp[0] = in[3] | in[1];
        temp[1] = in[3] | in[2];
    end

    assign out = temp;
    
endmodule
