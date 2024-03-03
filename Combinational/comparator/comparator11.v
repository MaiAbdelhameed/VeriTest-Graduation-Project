module comparator10(input A0,A1,B0,B1, output reg A_less_B, A_equal_B, A_greater_B);  

always @(*) begin
    case({A1,A0,B1,B0})
        4'b0000: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
        4'b0001: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b0010: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b0011: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b0100: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b0101: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
        4'b0110: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b0111: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b1000: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b1001: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b1010: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
        4'b1011: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        4'b1100: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b1101: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b1110: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        4'b1111: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
    endcase
end
endmodule   