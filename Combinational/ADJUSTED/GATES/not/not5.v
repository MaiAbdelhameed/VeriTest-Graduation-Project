module table_not (
  input in,
  output out
);

  table
    input in;
    output out;
  begin
    1'b0: out = 1'b1;
    1'b1: out = 1'b0;
  endtable

endmodule