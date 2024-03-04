module nor5 (
  input a,
  input b,
  output out
);

  table
    input a;
    input b;
    output out;
  begin
    1'b0 1'b0: 1'b1;
    1'b0 1'b1: 1'b0;
    1'b1 1'b0: 1'b0;
    1'b1 1'b1: 1'b0;
  endtable

endmodule
