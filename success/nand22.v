module nand22 (
    input wire a,
    output reg out
);

reg intermediate;

    always @(*) begin
        intermediate = a & a;
        out = ~intermediate;
    end

endmodule
