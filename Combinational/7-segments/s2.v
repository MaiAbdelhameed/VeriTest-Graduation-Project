module s2 (input [3:0] num,
                                      output [9:0] segments);

    reg [9:0] segment_map;

    // Define segment mappings for numbers 0-9
    always @(*) begin
        segment_map[0] = 7'b100_0000;
        segment_map[1] = 7'b111_1001;
        segment_map[2] = 7'b010_0100;
        segment_map[3] = 7'b011_0000;
        segment_map[4] = 7'b001_1001;
        segment_map[5] = 7'b001_0010;
        segment_map[6] = 7'b000_0010;
        segment_map[7] = 7'b111_1000;
        segment_map[8] = 7'b000_0000;
        segment_map[9] = 7'b001_0000;
    end
    
    assign segments = segment_map[num];
endmodule