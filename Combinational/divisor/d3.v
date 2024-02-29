module divisor_dataflow(input [1:0] a, b,
                        reg output [1:0] quotient, remainder);


    always @(*) begin
        quotient = a / b;
        remainder = a % b;
    end
endmodule