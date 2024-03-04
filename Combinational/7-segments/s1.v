module s1 (input [3:0] num,
                                      output [6:0] segments);

    wire [6:0] segment_map;

    // Define segment mappings for numbers 0-9
    assign segment_map[0] = 7'b100_0000;
    assign segment_map[1] = 7'b111_1001;
    assign segment_map[2] = 7'b010_0100;
    assign segment_map[3] = 7'b011_0000;
    assign segment_map[4] = 7'b001_1001;
    assign segment_map[5] = 7'b001_0010;
    assign segment_map[6] = 7'b000_0010;
    assign segment_map[7] = 7'b111_1000;
    assign segment_map[8] = 7'b000_0000;
    assign segment_map[9] = 7'b001_0000;

    assign segments = segment_map[num];
endmodule
