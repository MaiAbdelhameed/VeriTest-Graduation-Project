// tested
module and2_gate (
    input a,b,
    output reg out
);

    always @(*) begin
        out = &{a,b};
    end

endmodule