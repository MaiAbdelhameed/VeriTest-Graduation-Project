// tested
module nand7_gate (
    input wire a,
    input wire b,
    output reg out
);

    always @(*) begin
        out = ~(a & b) ? 1'b1 : 1'b0;
    end
    
endmodule
