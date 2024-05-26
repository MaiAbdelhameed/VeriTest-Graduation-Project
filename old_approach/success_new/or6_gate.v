// tested
module or6_gate (
    input wire a,b,
    output reg out
);

    always @(*) begin
        out = |{a,b};
    end
    
endmodule
