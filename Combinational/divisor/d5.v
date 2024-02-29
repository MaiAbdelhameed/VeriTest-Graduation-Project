module divisor_structural_loop(input [1:0] a, b,
                               output [1:0] quotient, remainder);

    wire [1:0] temp_remainder;
    wire [1:0] temp_quotient;

    reg [1:0] divisor;

    assign divisor = b;

    genvar i;
    generate
        for (i = 0; i < 2; i = i + 1) begin : generate_subtractor
            subtractor subtract(a, divisor, temp_quotient[i], temp_remainder);
        end
    endgenerate

    assign quotient = temp_quotient;
    assign remainder = temp_remainder;
endmodule

module subtractor(input [1:0] a, b,
                  output borrow, [1:0] difference);

    assign {borrow, difference} = a - b;
endmodule