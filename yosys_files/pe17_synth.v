/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "pe17.v:1.1-10.10" */
module pe17(i3, i2, i1, i0, o0, o1, v);
  wire _0_;
  wire _1_;
  /* src = "pe17.v:3.20-3.22" */
  input i0;
  wire i0;
  /* src = "pe17.v:3.17-3.19" */
  input i1;
  wire i1;
  /* src = "pe17.v:3.14-3.16" */
  input i2;
  wire i2;
  /* src = "pe17.v:3.11-3.13" */
  input i3;
  wire i3;
  /* src = "pe17.v:4.12-4.14" */
  output o0;
  wire o0;
  /* src = "pe17.v:4.15-4.17" */
  output o1;
  wire o1;
  /* src = "pe17.v:4.18-4.19" */
  output v;
  wire v;
  NOT _2_ (
    .A(i2),
    .Y(_0_)
  );
  AND _3_ (
    .A(_0_),
    .B(i1),
    .Y(_1_)
  );
  OR _4_ (
    .A(i3),
    .B(_1_),
    .Y(o0)
  );
  OR _5_ (
    .A(i2),
    .B(i3),
    .Y(o1)
  );
  OR _6_ (
    .A(i0),
    .B(o1),
    .Y(v)
  );
endmodule
