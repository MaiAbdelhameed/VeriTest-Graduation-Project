// tested
module and12_gate (
    input wire [3:0] a,
    input wire [3:0] b,
    output reg [3:0] out
);

integer i;

always @(*) begin
    for (i = 0; i < 4; i = i + 1) begin
        out[i] = a[i] & b[i];
    end
end


endmodule
