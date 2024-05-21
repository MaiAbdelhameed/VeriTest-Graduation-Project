module and28(
    input wire a,
    input wire b,
    output reg out
);

    always @(*) begin
        out = a && b;
    end
    
endmodule
