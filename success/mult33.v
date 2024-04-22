// CORRECT
module mult33 ( // Behavioral
    input [1:0] a,
    input [1:0] b,
    output reg [3:0] product
);

    always @(*) begin // Anything in the LHS inside always block MUST BE reg
      product = a * b;
    end

endmodule
