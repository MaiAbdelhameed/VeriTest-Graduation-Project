module nand_gate8 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = (a == 1'b0 || b == 1'b0) ? 1'b1 : 1'b0; // NAND using conditional expression
    end
endmodule
