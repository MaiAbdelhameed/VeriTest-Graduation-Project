// tested
module nand3 (
  input a,
  input b,
  output out
);

    wire temp;

    and (temp, a, b);
    not (out,temp);

endmodule
