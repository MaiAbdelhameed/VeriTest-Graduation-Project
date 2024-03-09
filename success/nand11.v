module nand11 (
    input wire [3:0] a,
    input wire [3:0] b,
    output reg [3:0] out
);

    always @(*) begin
        out = ~( {a[3] & b[3], a[2] & b[2], a[1] & b[1], a[0] & b[0]} );
    end
endmodule
