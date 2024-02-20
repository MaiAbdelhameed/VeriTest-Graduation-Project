module half_adder_basic_dataflow(input a, b,
                                 output sum, carry);

    assign sum = a ^ b;
    assign carry = a & b;

endmodule
