module mult10 (input a, b,
            output [1:0] result);

    reg [1:0] temp;

    always @(*) begin
        case ({a, b})
            2'b00: temp = 2'b00;
            2'b01: temp = 2'b00;
            2'b10: temp = 2'b00;
            2'b11: temp = 2'b01;
        endcase
    end

    assign result = temp;
endmodule