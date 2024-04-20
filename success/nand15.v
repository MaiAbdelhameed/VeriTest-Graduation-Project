module nand15 (
    input wire a,
    output reg out
);

    always @(*) begin
        out = ~(a & a);
    end

endmodule
