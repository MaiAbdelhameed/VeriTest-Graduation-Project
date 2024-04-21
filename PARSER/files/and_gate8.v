module and_gate8 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin
        case ({a, b})
            2'b00: temp = 1'b0;
            2'b01, 2'b10: temp = 1'b0;
            2'b11: temp = 1'b1;
        endcase
    end

    assign out = temp;

endmodule