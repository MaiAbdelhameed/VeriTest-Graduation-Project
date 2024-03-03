module unary_and_reduction(
    input wire a,
    output reg out
);

    always @(*) begin:
        out = &{a};
    end
endmodule
