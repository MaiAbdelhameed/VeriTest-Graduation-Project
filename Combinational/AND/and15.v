module and15 (
    input wire a,
    output reg out
);
    always @(*) begin : and
        out = (a & 1'b1);
    end

endmodule
