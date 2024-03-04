module mult11 (input a, b,
            output reg [1:0] result);


    always @(*) begin
        case ({a, b})
            2'b00: result = 2'b00;
            2'b01: result = 2'b00;
            2'b10: result = 2'b00;
            2'b11: result = 2'b01;
        endcase
    end

endmodule