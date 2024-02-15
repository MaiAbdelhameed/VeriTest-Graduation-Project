module table_half_adder (
  input a,
  input b,
  output sum,
  output carry
);

  table
    input a;
    input b;
    output sum;
    output carry;
  begin
    1'b0 1'b0: sum = 1'b0; carry = 1'b0;
    1'b0 1'b1: sum = 1'b1; carry = 1'b0;
    1'b1 1'b0: sum = 1'b1; carry = 1'b0;
    1'b1 1'b1: sum = 1'b0; carry = 1'b1;
  endtable

endmodule
