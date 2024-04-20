module and13 (
    input wire a,
    output reg out
);

    always @(*) begin
        out = (a == 1'b1);
    end
endmodule
