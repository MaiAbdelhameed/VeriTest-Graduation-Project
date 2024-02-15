module table_full_adder (
  input a,
  input b,
  input cin,
  output sum,
  output cout
);

  table
    input a;
    input b;
    input cin;
    output sum;
    output cout;
  begin
    1'b0 1'b0 1'b0: sum = 1'b0; cout = 1'b0;
    1'b0 1'b0 1'b1: sum = 1'b1; cout = 1'b0;
    1'b0 1'b1 1'b0: sum = 1'b1; cout = 1'b0;
    1'b0 1'b1 1'b1: sum = 1'b0; cout = 1'b1;
    1'b1 1'b0 1'b0: sum = 1'b1; cout = 1'b0;
    1'b1 1'b0 1'b1: sum = 1'b0; cout = 1'b1;
    1'b1 1'b1 1'b0: sum = 1'b0; cout = 1'b1;
    1'b1 1'b1 1'b1: sum = 1'b1; cout = 1'b1;
  endtable

endmodule
