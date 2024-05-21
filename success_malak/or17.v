//tested
module or17 (
    input [1:0] a,
    input [1:0] b,
    output [1:0] out
);


    always @(*) begin
        case ({a, b})
            4'b00_00: out = 2'b00;
            4'b00_01: out = 2'b01;
            4'b00_10: out = 2'b10;
            4'b00_11: out = 2'b11;
            4'b01_00: out = 2'b01;
            4'b01_01: out = 2'b01;
            4'b01_10: out = 2'b11;
            4'b01_11: out = 2'b11;
            4'b10_00: out = 2'b10;
            4'b10_01: out = 2'b11;
            4'b10_10: out = 2'b10;
            4'b10_11: out = 2'b11;
            4'b11_00: out = 2'b11;
            4'b11_01: out = 2'b11;
            4'b11_10: out = 2'b11;
            4'b11_11: out = 2'b11;
        endcase
    end
endmodule