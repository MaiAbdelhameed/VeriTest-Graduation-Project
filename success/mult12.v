module mult12 (input a, b,
            output result);

    reg temp;

    always @(*) begin
        case ({a, b})
            2'b00: temp = 1'b0;
            2'b01: temp = 1'b0;
            2'b10: temp = 1'b0;
            2'b11: temp = 1'b1;
        endcase
    end

    assign result = temp;
endmodule