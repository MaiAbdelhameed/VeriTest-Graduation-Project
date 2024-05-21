module mult9 (input a, b,
            output reg result); // tested


    always @(*) begin
        case ({a, b})
            2'b00: result = 1'b0;
            2'b01: result = 1'b0;
            2'b10: result = 1'b0;
            2'b11: result = 1'b1;
        endcase
    end
endmodule