module unary_and_bitwise(
    input wire a,
    output reg out
);

    always @(*) begin :
        out = &a;
    end

endmodule
