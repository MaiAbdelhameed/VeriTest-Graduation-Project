module s5 (input [3:0] num,
                                      output [6:0] segments);

    reg [6:0] segment_out;

    always @(*) begin
        case(num)
            4'b0000: segment_out = 7'b100_0000; // 0
            4'b0001: segment_out = 7'b111_1001; // 1
            4'b0010: segment_out = 7'b010_0100; // 2
            4'b0011: segment_out = 7'b011_0000; // 3
            4'b0100: segment_out = 7'b001_1001; // 4
            4'b0101: segment_out = 7'b001_0010; // 5
            4'b0110: segment_out = 7'b000_0010; // 6
            4'b0111: segment_out = 7'b111_1000; // 7
            4'b1000: segment_out = 7'b000_0000; // 8
            4'b1001: segment_out = 7'b001_0000; // 9
            default: segment_out = 7'bxxxxxxx; // Undefined
        endcase
    end

    assign segments = segment_out;
endmodule

