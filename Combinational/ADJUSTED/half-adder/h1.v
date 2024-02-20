module half_adder_basic_structural(input a, b,
                                   output sum, carry);

    xor xor_gate(sum, a, b);
    and and_gate(carry, a, b);

endmodule
