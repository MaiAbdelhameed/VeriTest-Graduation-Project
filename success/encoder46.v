module encoder46 (input [3:0] in, output [1:0] out);

    reg [1:0] temp;
    always @* begin
        case(in)
            4'b0001: temp = 2'b01;
            4'b0010: temp = 2'b10;
            4'b0100: temp = 2'b11;
            4'b1000: temp = 2'b00;
            default: temp = 2'b00; // Handle undefined case
        endcase
    end

    assign out = temp;

endmodule
