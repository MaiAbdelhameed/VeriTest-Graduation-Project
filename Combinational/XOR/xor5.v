module xor5 (
  input a,
  input b,
  output out
);

  table
    input {a, b};
    output out;
  begin
    1'b00: out = 1'b0;
    1'b01, 1'b10: out = 1'b1;
    1'b11: out = 1'b0;
  endtable

endmodule