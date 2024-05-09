module and_gate7 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        case ({a, b})
            2'b00: out = 1'b0;
            2'b01, 2'b10: out = 1'b0;
            2'b11: out = 1'b1;
        endcase
    end

endmodule