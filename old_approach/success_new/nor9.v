// tested
module nor9 (
    input a,
    input b,
    output reg result
);

always @(*) begin
    case ({a, b})
        2'b00: result = 1;
        2'b01: result = 0;
        2'b10: result = 0;
        2'b11: result = 0;
    endcase
end

endmodule
