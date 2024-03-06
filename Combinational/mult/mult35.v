module mult35 (input [1:0] a, input [1:0] b,
            output reg [3:0] result);

    always @(*) begin
        result[0] = a[0] & b[0];
        result[1] = ~a[1] & a[0] & b[1] + a[0] & b[1] & ~b[0] + a[1] & ~a[0] & b[0] + a[1] & b[0] & ~b[1];
        result[2] = a[1] & b[1] & ~b[0] + a[1] & ~a[0] & b[1];
        result[3] = a[1] & b[1] & a[0] & b[0];       
    end
endmodule
