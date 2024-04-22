module nor_gate6 (
  input a,
  input b,
  output reg out
);

    always @(*) begin
        out = ~(a | b); // NOR using built-in operator
    end

endmodule