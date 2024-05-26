module mux25 (input in0,in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,
                    in16,in17,in18,in19,in20,in21,in22,in23,in24,in25,in26,in27,in28,in29,in30,in31,
                            input [4:0] sel,
                            output reg out);

    always @(*) begin
        out = (sel == 5'b00000) ? in0 :
                    (sel == 5'b00001) ? in1 :
                    (sel == 5'b00010) ? in2 :
                    (sel == 5'b00011) ? in3 :
                    (sel == 5'b00100) ? in4 :
                    (sel == 5'b00101) ? in5 :
                    (sel == 5'b00110) ? in6 :
                    (sel == 5'b00111) ? in7 :
                    (sel == 5'b01000) ? in8 :
                    (sel == 5'b01001) ? in9 :
                    (sel == 5'b01010) ? in10 :
                    (sel == 5'b01011) ? in11 :
                    (sel == 5'b01100) ? in12 :
                    (sel == 5'b01101) ? in13 :
                    (sel == 5'b01110) ? in14 :
                    (sel == 5'b01111) ? in15 :
                    (sel == 5'b10000) ? in16 :
                    (sel == 5'b10001) ? in17 :
                    (sel == 5'b10010) ? in18 :
                    (sel == 5'b10011) ? in19 :
                    (sel == 5'b10100) ? in20 :
                    (sel == 5'b10101) ? in21 :
                    (sel == 5'b10110) ? in22 :
                    (sel == 5'b10111) ? in23 :
                    (sel == 5'b11000) ? in24 :
                    (sel == 5'b11001) ? in25 :
                    (sel == 5'b11010) ? in26 :
                    (sel == 5'b11011) ? in27 :
                    (sel == 5'b11100) ? in28 :
                    (sel == 5'b11101) ? in29 :
                    (sel == 5'b11110) ? in30 :
                    in31 ;
    end
    

endmodule