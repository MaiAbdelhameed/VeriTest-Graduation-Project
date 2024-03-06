module nor11 (
    input wire a,
    output reg out
);

    always @(*) begin
        out = (|a == 1'b0) ? 1'b1 : 1'b0;
    end


endmodule
