module mux67 (input [15:0] in,
                              input [3:0] sel,
                              output reg out);

    always @(*) begin
        out = (sel == 4'b0000) ? in[0] :
                    (sel == 4'b0001) ? in[1] :
                    (sel == 4'b0010) ? in[2] :
                    (sel == 4'b0011) ? in[3] :
                    (sel == 4'b0100) ? in[4] :
                    (sel == 4'b0101) ? in[5] :
                    (sel == 4'b0110) ? in[6] :
                    (sel == 4'b0111) ? in[7] :
                    (sel == 4'b1000) ? in[8] :
                    (sel == 4'b1001) ? in[9] :
                    (sel == 4'b1010) ? in[10] :
                    (sel == 4'b1011) ? in[11] :
                    (sel == 4'b1100) ? in[12] :
                    (sel == 4'b1101) ? in[13] :
                    (sel == 4'b1110) ? in[14] :
                    in[15];
    end

endmodule
