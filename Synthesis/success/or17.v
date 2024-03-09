module or17 (
    input wire a,
    output out
);

    reg temp;
    always @(*) begin
        temp = a | a;
    end
    
    assign out = temp;
endmodule
