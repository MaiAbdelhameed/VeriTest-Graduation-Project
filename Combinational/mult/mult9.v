module mult9 (input [1:0] a, b,
            output [3:0] result);

    reg [3:0] temp;
    
    always @(*) begin
        temp[0] = a[0] & b[0];
        temp[1] = ~a[1] & a[0] & b[1] + a[0] & b[1] & ~b[0] + a[1] & ~a[0] & b[0] + a[1] & b[0] & ~b[1];
        temp[2] = a[1] & b[1] & ~b[0] + a[1] & ~a[0] & b[1];
        temp[3] = a[1] & b[1] & a[0] & b[0];       
    end

    assign result = temp;
endmodule