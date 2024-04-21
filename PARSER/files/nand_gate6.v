module nand_gate6 (
  input a,
  input b,
  output reg out
);
    always @(*) begin
        out = ~(a & b); // NAND using built-in operator
    end
endmodule
