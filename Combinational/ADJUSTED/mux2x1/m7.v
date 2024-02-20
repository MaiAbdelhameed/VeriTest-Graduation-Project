module mux_behavioral_table(input a, b, sel,
                            output y);

    always @(*) begin
        case ({sel, a, b})
            3'b000: y = 1'b0;
            3'b001: y = b;
            3'b010: y = a;
            3'b011: y = 1'b1;
            3'b100: y = 1'b0;
            3'b101: y = 1'b1;
            3'b110: y = 1'b1;
            3'b111: y = 1'b1;
            default: y = 1'bx;
        endcase
    end

endmodule