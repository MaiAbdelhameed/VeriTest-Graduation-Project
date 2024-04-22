module nand_gate9 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin
        temp = (a == 1'b0 || b == 1'b0) ? 1'b1 : 1'b0; // NAND using conditional expression
    end

    assign out = temp;
endmodule