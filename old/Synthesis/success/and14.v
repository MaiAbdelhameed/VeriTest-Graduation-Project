module and14 (
    input wire a,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = (a == 1'b1);
    end
    
    assign out = temp;
endmodule
