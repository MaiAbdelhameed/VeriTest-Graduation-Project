module nor14 (
    input wire a,
    output wire out
);


    reg temp;
    always @(*) begin
        if (|a == 1'b0)
            temp = 1'b1;
        else
            temp = 1'b0;
    end

    assign out = temp;
    
endmodule
