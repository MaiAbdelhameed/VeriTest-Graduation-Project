// tested
module nor8_gate (
    input a,
    input b,
    output result
);

    reg temp;
always @(*) begin
    case ({a, b})
        2'b00: temp = 0;
        2'b01: temp = 1;
        2'b10: temp = 1;
        2'b11: temp = 1;
    endcase
end

    assign result = ~temp;

endmodule
