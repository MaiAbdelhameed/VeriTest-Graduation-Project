module xor13 (
  input a,
  input b,
  output wire out
);

reg temp;
always @(*) begin
    case ({a, b})
        2'b00, 2'b11: temp = 1'b0; // Both bits same
        2'b01, 2'b10: temp = 1'b1; // Bits different
    endcase
end
assign out = temp;
endmodule