module or19 (
    input wire a,
    output reg out
);

    always @(*) begin
        out = |a;
    end
    
endmodule
