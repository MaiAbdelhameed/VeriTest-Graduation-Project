module mult8 (input a1,a0,b1,b0,
            output reg [3:0] result);

    always @(*) begin
        result[0] = a0 & b0;
        result[1] = ~a1 & a0 & b1 + a0 & b1 & ~b0 + a1 & ~a0 & b0 + a1 & b0 & ~b1;
        result[2] = a1 & b1 & ~b0 + a1 & ~a0 & b1;
        result[3] = a1 & b1 & a0 & b0;       
    end
endmodule
