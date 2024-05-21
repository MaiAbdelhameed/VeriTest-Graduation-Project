// tested
module and2 (
    input a,b,
    output reg out
);

    always @(*) begin
        out = &{a,b};
    end

endmodule