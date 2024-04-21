module d3 (input [1:0] a,input [1:0] b,
                    output reg [1:0] quotient, output reg [1:0] remainder);


    always @(*) begin
        quotient = a / b;
        remainder = a % b;
    end
endmodule
Error occurred: 'Divide' object has no attribute 'name'