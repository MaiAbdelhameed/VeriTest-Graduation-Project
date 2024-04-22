module and15 (
    input a,
    output reg out
);
    always @(*) begin
        out = (a & 1'b1);
    end

endmodule