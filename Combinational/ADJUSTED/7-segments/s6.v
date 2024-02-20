module seven_segment_basic_behavioral(input [3:0] num,
                                      reg output [6:0] segments);

    always @(*) begin
        case(num)
            4'b0000: segments = 7'b100_0000; // 0
            4'b0001: segments = 7'b111_1001; // 1
            4'b0010: segments = 7'b010_0100; // 2
            4'b0011: segments = 7'b011_0000; // 3
            4'b0100: segments = 7'b001_1001; // 4
            4'b0101: segments = 7'b001_0010; // 5
            4'b0110: segments = 7'b000_0010; // 6
            4'b0111: segments = 7'b111_1000; // 7
            4'b1000: segments = 7'b000_0000; // 8
            4'b1001: segments = 7'b001_0000; // 9
            default: segments = 7'bxxxxxxx; // Undefined
        endcase
    end

endmodule


