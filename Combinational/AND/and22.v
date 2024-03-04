module and22 (
    input wire a,
    output wire out
);

reg result;

always @(*) begin
    result = 1'b1;
    for (int i = 0; i < $bits(a); i = i + 1) begin
        result = result & a[i];
    end
end

assign out = result;

endmodule
