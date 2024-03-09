module d9 (input [1:0] a, b,
                                output [1:0] quotient, remainder);

    reg [1:0] temp_quotient;
    reg [1:0] temp_remainder;

    always @(*) begin
        case ({a, b})

            4'b00_00: begin temp_quotient = 2'b00; temp_remainder = 2'b00; end
            4'b00_01: begin temp_quotient = 2'bxx; temp_remainder = 2'b00; end
            4'b00_10: begin temp_quotient = 2'b00; temp_remainder = 2'bxx; end
            4'b00_11: begin temp_quotient = 2'b01; temp_remainder = a; end
            4'b01_00: begin temp_quotient = 2'b00; temp_remainder = 2'b00; end
            4'b01_01: begin temp_quotient = 2'b01; temp_remainder = 2'b00; end
            4'b01_10: begin temp_quotient = 2'b10; temp_remainder = a - 2'b10; end
            4'b01_11: begin temp_quotient = 2'b11; temp_remainder = a - 2'b11; end
            4'b10_00: begin temp_quotient = 2'b00; temp_remainder = 2'b00; end
            4'b10_01: begin temp_quotient = 2'b10; temp_remainder = 2'b00; end
            4'b10_10: begin temp_quotient = 2'b01; temp_remainder = 2'bxx; end
            4'b10_11: begin temp_quotient = 2'b11; temp_remainder = a - 2'b11; end
            4'b11_00: begin temp_quotient = 2'b00; temp_remainder = 2'b00; end
            4'b11_01: begin temp_quotient = 2'b11; temp_remainder = 2'b00; end
            4'b11_10: begin temp_quotient = 2'b10; temp_remainder = 2'bxx; end
            4'b11_11: begin temp_quotient = 2'b11; temp_remainder = a - 2'b11; end
            
            default: begin temp_quotient = 2'bxx; temp_remainder = 2'bxx; end
        endcase
    end

    assign quotient = temp_quotient;
    assign remainder = temp_remainder;
endmodule