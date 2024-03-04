module s4 (input [3:0] num,
                                    output [6:0] segments);

    assign segments[0] = (num == 4'b0000) ? 1'b1 : 1'b0;
    assign segments[1] = (num == 4'b0001) ? 1'b1 : 1'b0;
    assign segments[2] = (num == 4'b0010) ? 1'b1 : 1'b0;
    assign segments[3] = (num == 4'b0011) ? 1'b1 : 1'b0;
    assign segments[4] = (num == 4'b0100) ? 1'b1 : 1'b0;
    assign segments[5] = (num == 4'b0101) ? 1'b1 : 1'b0;
    assign segments[6] = (num == 4'b0110) ? 1'b1 : 1'b0;
    assign segments[7] = (num == 4'b0111) ? 1'b1 : 1'b0;
    assign segments[8] = (num == 4'b1000) ? 1'b1 : 1'b0;
    assign segments[9] = (num == 4'b1001) ? 1'b1 : 1'b0;
endmodule
