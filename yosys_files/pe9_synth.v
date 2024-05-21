/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "pe9.v:1.1-14.10" */
module pe9(D0, D1, D2, D3, Y1, Y0, V);
  wire _0_;
  wire _1_;
  wire _2_;
  /* src = "pe9.v:3.11-3.13" */
  input D0;
  wire D0;
  /* src = "pe9.v:3.14-3.16" */
  input D1;
  wire D1;
  /* src = "pe9.v:3.17-3.19" */
  input D2;
  wire D2;
  /* src = "pe9.v:3.20-3.22" */
  input D3;
  wire D3;
  /* src = "pe9.v:4.22-4.23" */
  output V;
  wire V;
  /* src = "pe9.v:4.19-4.21" */
  output Y0;
  wire Y0;
  /* src = "pe9.v:4.16-4.18" */
  output Y1;
  wire Y1;
  NOT _3_ (
    .A(D2),
    .Y(_2_)
  );
  OR _4_ (
    .A(D2),
    .B(D3),
    .Y(Y1)
  );
  AND _5_ (
    .A(D1),
    .B(_2_),
    .Y(_0_)
  );
  OR _6_ (
    .A(D3),
    .B(_0_),
    .Y(Y0)
  );
  OR _7_ (
    .A(D0),
    .B(D1),
    .Y(_1_)
  );
  OR _8_ (
    .A(Y1),
    .B(_1_),
    .Y(V)
  );
endmodule
