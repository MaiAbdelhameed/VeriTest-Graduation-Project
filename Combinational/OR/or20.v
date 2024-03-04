module or20 (
    input wire a,
    output reg out
);

    reg temp;
    always @(*) begin:
        temp = |a;
    end
    
    assign out = temp;
endmodule
