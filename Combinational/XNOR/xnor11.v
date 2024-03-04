module xnor11 (
    input wire a,
    input wire b,
    output reg out
);

    always @(*) begin:
        out = ~(a ^ b);
    end
    
endmodule
