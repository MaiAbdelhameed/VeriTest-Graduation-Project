/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "decoder10.v:1.1-26.10" */
module decoder10(ip0, ip1, op0, op1, op2, op3);
  wire _0_;
  wire _1_;
  wire _2_;
  /* src = "decoder10.v:3.7-3.10" */
  input ip0;
  wire ip0;
  /* src = "decoder10.v:3.11-3.14" */
  input ip1;
  wire ip1;
  /* src = "decoder10.v:4.12-4.15" */
  output op0;
  wire op0;
  /* src = "decoder10.v:4.16-4.19" */
  output op1;
  wire op1;
  /* src = "decoder10.v:4.20-4.23" */
  output op2;
  wire op2;
  /* src = "decoder10.v:4.24-4.27" */
  output op3;
  wire op3;
  not _3_ (
    .A(ip1),
    .Y(_0_)
  );
  not _4_ (
    .A(ip0),
    .Y(_1_)
  );
  OR _5_ (
    .A(ip1),
    .B(ip0),
    .Y(_2_)
  );
  not _6_ (
    .A(_2_),
    .Y(op0)
  );
  AND _7_ (
    .A(_0_),
    .B(ip0),
    .Y(op1)
  );
  AND _8_ (
    .A(ip1),
    .B(ip0),
    .Y(op3)
  );
  AND _9_ (
    .A(ip1),
    .B(_1_),
    .Y(op2)
  );
endmodule