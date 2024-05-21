module mult7 (input [1:0] a, b,
            output reg [3:0] result); // tested

    reg a0b1;
    reg a1b0;
    reg a1b1;
    reg a1b0_a0b1;
    
    always @(*) begin
        result[0] = a[0] & b[0];
        a0b1 = a[0] & b[1];
        a1b0 = a[1] & b[0];
        a1b1 = a[1] & b[1];
        result[1] = (~a1b0 & a0b1) | (a1b0 & ~a0b1);
        a1b0_a0b1 = a1b0 & a0b1;
        result[2] = (~a1b1 & a1b0_a0b1) | (a1b1 & ~a1b0_a0b1);
        result[3] = a1b1 & a1b0_a0b1;      
    end

endmodule