module divisor_dataflow_kmap(input [1:0] a, b,
                             output [1:0] quotient, remainder);

    assign quotient[0] = a[0] ^ b[0];
    assign quotient[1] = (a[1] & !b[1]) | (a[0] & b[0]);
    assign remainder = a % b;
endmodule
