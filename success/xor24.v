module xor24 (
    input wire [3:0] a,
    output reg out
);

    always @(*) begin
        out = (^a == 1'b1) ? 1'b1 : 1'b0;
    end
    
endmodule
