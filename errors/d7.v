module d7 (input [1:0] a, input [1:0]  b,
                            output reg [1:0] quotient, output reg [1:0] remainder);

    always @(*) begin
        quotient[0] = a[0] ^ b[0];
        quotient[1] = (a[1] & !b[1]) | (a[0] & b[0]);
        remainder = a % b;
    end
    
endmodule

Error occurred: 'Mod' object has no attribute 'name'