///4x2
module encoder39 (input [3:0] in, output reg [1:0] out);

    reg [1:0] temp;
    always @(*) begin 
        temp = (in[3]) ? 2'b11 : (in[2]) ? 2'b10 : (in[1]) ? 2'b01 : (in[0]) ? 2'b00 : 2'b00;
    end

endmodule
