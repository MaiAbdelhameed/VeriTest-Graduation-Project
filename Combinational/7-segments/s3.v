module s3 (input [3:0] num,
                                      reg output [6:0] segments);

    always @(*) begin
        // Define segment mappings for numbers 0-9
        segments[0] = 7'b100_0000;
        segments[1] = 7'b111_1001;
        segments[2] = 7'b010_0100;
        segments[3] = 7'b011_0000;
        segments[4] = 7'b001_1001;
        segments[5] = 7'b001_0010;
        segments[6] = 7'b000_0010;
        segments[7] = 7'b111_1000;
        segments[8] = 7'b000_0000;
        segments[9] = 7'b001_0000;
    end
    

endmodule
