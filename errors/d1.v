module d1 (input [1:0] a, b,
                          output [1:0] quotient, remainder);

    wire [1:0] temp_remainder;
    wire [1:0] temp_quotient;

    assign temp_remainder = a % b;
    assign temp_quotient = a / b;

    assign quotient = temp_quotient;
    assign remainder = temp_remainder;
endmodule
Error occurred: 'Mod' object has no attribute 'name'