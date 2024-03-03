module unary_and(
    input wire a,
    output wire out
);

    always @(*) begin
        case (a)
            1'b0: out = 1'b0;
            default: out = 1'b1;
        endcase
    end

endmodule
