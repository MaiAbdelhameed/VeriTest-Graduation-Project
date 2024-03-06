module xor25 (
    input wire [3:0] a,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = (^a == 1'b1) ? 1'b1 : 1'b0;
    end
    
    assign out = temp;
endmodule
