module comparator12 (input A,B, output reg A_less_B, A_equal_B, A_greater_B);  

always @(*) begin
    case({A,B})
        2'b00: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
        2'b01: {A_greater_B,A_equal_B,A_less_B} = 3'b001;
        2'b10: {A_greater_B,A_equal_B,A_less_B} = 3'b100;
        2'b11: {A_greater_B,A_equal_B,A_less_B} = 3'b010;
    endcase
end
endmodule   
Error occurred: 'NoneType' object has no attribute 'connections'