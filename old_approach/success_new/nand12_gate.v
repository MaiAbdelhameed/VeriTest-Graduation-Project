// tested
module nand12_gate (
    input wire a,
    input wire b,
    output reg out
);

    always @(*) begin
        out = ~&{a, b};
    end
    
endmodule
