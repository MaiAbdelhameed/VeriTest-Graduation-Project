// tested
module and19 (
    input wire [1:0] a,
    input wire [1:0] b,
    output reg [1:0] out
);
    always @(*) begin
        out[1] = a[1] & b[1];
        out[0] = a[0] & b[0];
    end

endmodule
