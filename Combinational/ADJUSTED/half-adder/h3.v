module half_adder_basic_dataflow(input a, b,
                                 reg output sum, carry);

    always @(*) begin
        sum = a ^ b;
        carry = a & b;
    end

endmodule
