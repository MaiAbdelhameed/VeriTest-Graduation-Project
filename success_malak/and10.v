// tested
module and10 (
  input a,
  input b,
  output out
);

    wire temp;
    nand (temp,a,b);
    not(out,temp);

endmodule