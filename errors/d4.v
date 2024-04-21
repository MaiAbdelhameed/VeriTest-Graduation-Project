module d4 (input [1:0] a, b,
                        output [1:0] quotient, remainder);


    reg [1:0] temp_quotient;
    reg [1:0] temp_remainder;

    always @(*) begin
        temp_quotient = a / b;
        temp_remainder = a % b;
    end

    assign quotient = temp_quotient;
    assign remainder = temp_remainder;
endmodule
Error occurred: 'Divide' object has no attribute 'name'