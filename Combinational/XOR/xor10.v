module xor10 (
  input a,
  input b,
  output reg out
);

always @(*) begin
    case ({a, b})
        2'b00, 2'b11: out = 1'b0; // Both bits same
        2'b01, 2'b10: out = 1'b1; // Bits different
    endcase
end
endmodule

