module and_gate12 (
    input wire a,
    output reg out
);

    always @(*) begin
        case (a)
            1'b0: out = 1'b0;
            default: out = 1'b1;
        endcase
    end

endmodule
