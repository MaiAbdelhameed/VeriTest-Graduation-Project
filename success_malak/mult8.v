module mult8 (input a0,a1, b0,b1,
            output reg [3:0] result); //tested 

    reg a0b1;
    reg a1b0;
    reg a1b1;
    reg a1b0_a0b1;
    
    always @(*) begin
        result[0] = a0 & b0;
        a0b1 = a0 & b1;
        a1b0 = a1 & b0;
        a1b1 = a1 & b1;
        result[1] = (~a1b0 & a0b1) | (a1b0 & ~a0b1);
        a1b0_a0b1 = a1b0 & a0b1;
        result[2] = (~a1b1 & a1b0_a0b1) | (a1b1 & ~a1b0_a0b1);
        result[3] = a1b1 & a1b0_a0b1;      
    end

endmodule