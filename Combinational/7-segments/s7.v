module seven_segment_structural_loop(input [3:0] num,
                                     output [6:0] segments);

    wire [6:0] segment_out;

    genvar i;
    generate
        for (i = 0; i < 10; i = i + 1) begin : generate_segments
            assign segment_out = (num == i) ? segment_map[i] : 7'bxxxxxxx;
        end
    endgenerate

    assign segments = segment_out;
endmodule
