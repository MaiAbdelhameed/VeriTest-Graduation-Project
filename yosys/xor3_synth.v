/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xor3.v:2.1-12.10" */
module xor3(a, b, out);
  wire _0_;
  wire _1_;
  wire _2_;
  /* src = "xor3.v:3.9-3.10" */
  input a;
  wire a;
  /* src = "xor3.v:4.9-4.10" */
  input b;
  wire b;
  /* src = "xor3.v:5.14-5.17" */
  output out;
  wire out;
  OR _3_ (
    .A(a),
    .B(b),
    .Y(_0_)
  );
  AND _4_ (
    .A(a),
    .B(b),
    .Y(_1_)
  );
  not _5_ (
    .A(_1_),
    .Y(_2_)
  );
  AND _6_ (
    .A(_0_),
    .B(_2_),
    .Y(out)
  );
endmodule