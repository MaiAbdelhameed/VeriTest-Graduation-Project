module d8 (input [1:0] a, b,
                            output [1:0] quotient, remainder);

    reg [1:0] temp_quotient;
    reg [1:0] temp_remainder;

    always @(*) begin
        temp_quotient[0] = a[0] ^ b[0];
        temp_quotient[1] = (a[1] & !b[1]) | (a[0] & b[0]);
        temp_remainder = a % b;
    end

    assign quotient = temp_quotient;
    assign remainder = temp_remainder;
    
endmodule
