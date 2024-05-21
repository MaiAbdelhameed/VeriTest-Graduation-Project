module mux23 (input [31:0] in,
                            input [4:0] sel,
                            output reg out);

    always @(*) begin
        out = (sel == 5'b00000) ? in[0] :
                    (sel == 5'b00001) ? in[1] :
                    (sel == 5'b00010) ? in[2] :
                    (sel == 5'b00011) ? in[3] :
                    (sel == 5'b00100) ? in[4] :
                    (sel == 5'b00101) ? in[5] :
                    (sel == 5'b00110) ? in[6] :
                    (sel == 5'b00111) ? in[7] :
                    (sel == 5'b01000) ? in[8] :
                    (sel == 5'b01001) ? in[9] :
                    (sel == 5'b01010) ? in[10] :
                    (sel == 5'b01011) ? in[11] :
                    (sel == 5'b01100) ? in[12] :
                    (sel == 5'b01101) ? in[13] :
                    (sel == 5'b01110) ? in[14] :
                    (sel == 5'b01111) ? in[15] :
                    (sel == 5'b10000) ? in[16] :
                    (sel == 5'b10001) ? in[17] :
                    (sel == 5'b10010) ? in[18] :
                    (sel == 5'b10011) ? in[19] :
                    (sel == 5'b10100) ? in[20] :
                    (sel == 5'b10101) ? in[21] :
                    (sel == 5'b10110) ? in[22] :
                    (sel == 5'b10111) ? in[23] :
                    (sel == 5'b11000) ? in[24] :
                    (sel == 5'b11001) ? in[25] :
                    (sel == 5'b11010) ? in[26] :
                    (sel == 5'b11011) ? in[27] :
                    (sel == 5'b11100) ? in[28] :
                    (sel == 5'b11101) ? in[29] :
                    (sel == 5'b11110) ? in[30] :
                    in[31] ;
    end
    

endmodule