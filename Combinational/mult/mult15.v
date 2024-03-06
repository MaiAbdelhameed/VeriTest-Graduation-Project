module mult15 (input a1,a0,b1,b0,
            output reg [3:0] result);

reg temp,temp2;

    always @(*) begin
        result[0] = a0 & b0;
        result[1] = (a0 & b1) ^ (a1 & b0);
        temp = ((a1 & b0) & (a0 & b1));
        temp2 = a1 & b1;
        result[2] = temp ^ temp2;
        result[3] = temp & temp2;       
    end
endmodule
