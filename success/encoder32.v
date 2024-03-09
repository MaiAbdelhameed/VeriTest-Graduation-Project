module encoder32 (input [1:0] in, output reg [1:0] out);

    always @* begin
        case(in)
            2'b01: out = 2'b01;
            2'b10: out = 2'b10;
        endcase
    end

endmodule
