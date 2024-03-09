module nand20 (
    input wire a,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = (a & a) ? 1'b0 : 1'b1;
    end
    
    assign out = temp;
    
endmodule
