module or27 (
    input wire [3:0] a,
    output wire out
);

reg result;

always @(*) begin
    result = 1'b0;
    for (int i = 0; i < 4; i = i + 1) begin
        result = result | a[i];
    end
end

assign out = result;

endmodule
