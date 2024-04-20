module and24 (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire [3:0] out
);

reg [3:0] result;
integer i;

always @(*) begin
    for (i = 0; i < 4; i = i + 1) begin
        result[i] = a[i] & b[i];
    end
end

assign out = result;

endmodule

Error occurred: 'ForStatement' object has no attribute 'name'