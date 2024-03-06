module and29(
    input wire a,
    input wire b,
    output wire out
);

    reg temp;
    always @(*) begin
        temp = a && b;
    end
    
    assign out = temp;
endmodule
