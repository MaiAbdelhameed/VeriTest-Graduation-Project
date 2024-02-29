module half_adder_basic_dataflow(input a, b,
                                 reg output sum, carry);
    reg temp_sum;
    reg temp_carry;

    always @(*) begin
        temp_sum = a ^ b;
        temp_carry = a & b;
    end
    
    assign sum = temp_sum;
    assign carry = temp_carry;
endmodule
