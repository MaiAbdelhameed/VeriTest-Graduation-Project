module divisor_dataflow(input [1:0] a, b,
                        output [1:0] quotient, remainder);

    assign quotient = a / b;
    assign remainder = a % b;
endmodule