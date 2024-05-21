module mult3 (input [1:0] a, b,
            output reg [3:0] result);


    always @(*) begin
        case ({a, b})
            4'b00_00: result = 4'b0000;
            4'b00_01: result = 4'b0000;
            4'b00_10: result = 4'b0000;
            4'b00_11: result = 4'b0000;
            4'b01_00: result = 4'b0000;
            4'b01_01: result = 4'b0001;
            4'b01_10: result = 4'b0010;
            4'b01_11: result = 4'b0011;
            4'b10_00: result = 4'b0000;
            4'b10_01: result = 4'b0010;
            4'b10_10: result = 4'b0100;
            4'b10_11: result = 4'b0110;
            4'b11_00: result = 4'b0000;
            4'b11_01: result = 4'b0011;
            4'b11_10: result = 4'b0110;
            4'b11_11: result = 4'b1001;
        endcase
    end
endmodule