// tested
module nand3_gate (
  input a,
  input b,
  output out
);

    wire temp;

    and (temp, a, b);
    not (out,temp);

endmodule
