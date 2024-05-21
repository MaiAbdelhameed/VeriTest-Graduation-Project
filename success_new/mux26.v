module mux26 (input in0,in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,
                            input [3:0] sel,
                            output reg out);

    always @(*) begin
        out = (sel == 4'b0000) ? in0 :
                    (sel == 4'b0001) ? in1 :
                    (sel == 4'b0010) ? in2 :
                    (sel == 4'b0011) ? in3 :
                    (sel == 4'b0100) ? in4 :
                    (sel == 4'b0101) ? in5 :
                    (sel == 4'b0110) ? in6 :
                    (sel == 4'b0111) ? in7 :
                    (sel == 4'b1000) ? in8 :
                    (sel == 4'b1001) ? in9 :
                    (sel == 4'b1010) ? in10 :
                    (sel == 4'b1011) ? in11 :
                    (sel == 4'b1100) ? in12 :
                    (sel == 4'b1101) ? in13 :
                    (sel == 4'b1110) ? in14 :
                    in15 ;
    end
    

endmodule