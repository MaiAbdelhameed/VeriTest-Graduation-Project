module and22 (
    input wire a,
    output wire out
);

reg result;
integer i;

always @(*) begin
    result = 1'b1;
    for (i = 0; i < $bits(a); i = i + 1) begin
        result = result & a[i];
    end
end

assign out = result;

endmodule

