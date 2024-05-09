module mult17 (
    input [1:0] a,
    input [2:0] b,
    output reg [4:0] result
);

always @(*) begin
    case ({a, b})
        5'b00_000: result = 5'b00000;
        5'b00_001: result = 5'b00000;
        5'b00_010: result = 5'b00000;
        5'b00_011: result = 5'b00000;
        5'b01_000: result = 5'b00000;
        5'b01_001: result = 5'b00001;
        5'b01_010: result = 5'b00010;
        5'b01_011: result = 5'b00011;
        5'b10_000: result = 5'b00000;
        5'b10_001: result = 5'b00010;
        5'b10_010: result = 5'b00100;
        5'b10_011: result = 5'b00110;
        5'b11_000: result = 5'b00000;
        5'b11_001: result = 5'b00011;
        5'b11_010: result = 5'b00110;
        5'b11_011: result = 5'b01001;
        5'b00_100: result = 5'b00000;
        5'b01_100: result = 5'b00100;
        5'b10_100: result = 5'b01000;
        5'b11_100: result = 5'b01100;
        5'b00_101: result = 5'b00000;
        5'b01_101: result = 5'b00101;
        5'b10_101: result = 5'b01010;
        5'b11_101: result = 5'b01111;
        5'b00_110: result = 5'b00000;
        5'b01_110: result = 5'b00110;
        5'b10_110: result = 5'b01100;
        5'b11_110: result = 5'b10010;
        5'b00_111: result = 5'b00000;
        5'b01_111: result = 5'b00111;
        5'b10_111: result = 5'b01110;
        5'b11_111: result = 5'b10101;
    endcase
end

endmodule
