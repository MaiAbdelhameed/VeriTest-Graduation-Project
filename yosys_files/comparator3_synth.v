/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "comparator3.v:1.1-9.10" */
module comparator3(A, B, C, D, E);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  /* src = "comparator3.v:2.11-2.12" */
  input A;
  wire A;
  /* src = "comparator3.v:2.13-2.14" */
  input B;
  wire B;
  /* src = "comparator3.v:3.12-3.13" */
  output C;
  wire C;
  /* src = "comparator3.v:3.14-3.15" */
  output D;
  wire D;
  /* src = "comparator3.v:3.16-3.17" */
  output E;
  wire E;
  NOT _04_ (
    .A(A),
    .Y(_01_)
  );
  NOT _05_ (
    .A(B),
    .Y(_02_)
  );
  OR _06_ (
    .A(A),
    .B(_02_),
    .Y(_03_)
  );
  NOT _07_ (
    .A(_03_),
    .Y(C)
  );
  OR _08_ (
    .A(_01_),
    .B(B),
    .Y(_00_)
  );
  NOT _09_ (
    .A(_00_),
    .Y(E)
  );
  AND _10_ (
    .A(_03_),
    .B(_00_),
    .Y(D)
  );
endmodule
