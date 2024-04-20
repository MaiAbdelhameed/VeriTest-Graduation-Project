module decoder38 (input [1:0] in, output [3:0] out);

    reg [3:0] temp;
    always @* begin
        case(in)
            2'b00: temp = 4'b0001;
            2'b01: temp = 4'b0010;
            2'b10: temp = 4'b0100;
            default: temp = 4'b1000;
        endcase
    end


    assign out = temp;
    
endmodule
