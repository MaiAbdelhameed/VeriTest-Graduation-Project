module nand19 (
    input wire a,
    output reg out
);

    always @(*) begin
        out = (a & a) ? 1'b0 : 1'b1;
    end
    
endmodule
