module xnor23 (
    input wire a,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = (a ^ a == 1'b0) ? 1'b1 : 1'b0;
    end

    assign out = temp;
endmodule
