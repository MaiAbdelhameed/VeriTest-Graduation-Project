module nand_gate7 (
  input a,
  input b,
  output out
);

    reg temp;
    always @(*) begin
        temp = ~(a & b); // NAND using built-in operator
    end

    assign out = temp;
endmodule
