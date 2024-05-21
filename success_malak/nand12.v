// tested
module nand12 (
    input wire a,b,
    output reg out
);

    always @(*) begin
        out = ~&{a, b};
    end
    
endmodule
