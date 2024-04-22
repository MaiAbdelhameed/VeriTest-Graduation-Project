// CORRECT
module mult6 (input [1:0] a, b,
            output [3:0] result);

    reg [3:0] temp;

    always @(*) begin
        temp = a * b;
    end

    assign result = temp;
endmodule