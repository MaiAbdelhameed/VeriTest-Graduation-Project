/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "and20.v:3.1-12.10" */
module and20(a, b, c, out);
  wire _0_;
  /* src = "and20.v:4.9-4.10" */
  input a;
  wire a;
  /* src = "and20.v:5.9-5.10" */
  input b;
  wire b;
  /* src = "and20.v:6.9-6.10" */
  input c;
  wire c;
  /* src = "and20.v:7.10-7.13" */
  output out;
  wire out;
  AND _1_ (
    .A(a),
    .B(b),
    .Y(_0_)
  );
  AND _2_ (
    .A(c),
    .B(_0_),
    .Y(out)
  );
endmodule