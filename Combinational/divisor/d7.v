module d7 (input [1:0] a, b,
                            reg output [1:0] quotient, remainder);

    always @(*) begin
        quotient[0] = a[0] ^ b[0];
        quotient[1] = (a[1] & !b[1]) | (a[0] & b[0]);
        remainder = a % b;
    end
    
endmodule
