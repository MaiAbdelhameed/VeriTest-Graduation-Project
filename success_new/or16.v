//tested
module or16 (
    input [1:0] a,b,
    output reg [1:0] out
);

    always @(*) begin
        out[0] = (|{a[0],b[0]} == 1'b0) ? 1'b0 : 1'b1;
        out[1] = (|{a[1],b[1]} == 1'b0) ? 1'b0 : 1'b1;
    end
    
endmodule
