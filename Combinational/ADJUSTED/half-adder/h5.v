module half_adder_structural_loop(input a, b,
                                  output sum, carry);

    wire [1:0] temp;

    genvar i;
    generate
        for (i = 0; i < 2; i = i + 1) begin : generate_xor_and
            xor xor_gate(temp[i], a[i], b[i]);
        end
    endgenerate

    and and_gate(carry, a, b);
    assign sum = temp[0];

endmodule
