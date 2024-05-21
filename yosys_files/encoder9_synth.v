/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "encoder9.v:1.1-18.10" */
module encoder9(a, en, y);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  wire _08_;
  wire _09_;
  wire _10_;
  wire _11_;
  wire _12_;
  /* src = "encoder9.v:2.17-2.18" */
  input [3:0] a;
  wire [3:0] a;
  /* src = "encoder9.v:3.11-3.13" */
  input en;
  wire en;
  /* src = "encoder9.v:4.22-4.23" */
  output [1:0] y;
  wire [1:0] y;
  NOT _13_ (
    .A(a[2]),
    .Y(_11_)
  );
  NOT _14_ (
    .A(a[0]),
    .Y(_12_)
  );
  AND _15_ (
    .A(_12_),
    .B(en),
    .Y(_00_)
  );
  AND _16_ (
    .A(_11_),
    .B(_00_),
    .Y(_01_)
  );
  OR _17_ (
    .A(a[1]),
    .B(a[3]),
    .Y(_02_)
  );
  AND _18_ (
    .A(a[1]),
    .B(a[3]),
    .Y(_03_)
  );
  NOT _19_ (
    .A(_03_),
    .Y(_04_)
  );
  AND _20_ (
    .A(_02_),
    .B(_04_),
    .Y(_05_)
  );
  AND _21_ (
    .A(_01_),
    .B(_05_),
    .Y(y[0])
  );
  AND _22_ (
    .A(a[2]),
    .B(a[3]),
    .Y(_06_)
  );
  OR _23_ (
    .A(a[2]),
    .B(a[3]),
    .Y(_07_)
  );
  OR _24_ (
    .A(a[1]),
    .B(_06_),
    .Y(_08_)
  );
  NOT _25_ (
    .A(_08_),
    .Y(_09_)
  );
  AND _26_ (
    .A(_00_),
    .B(_07_),
    .Y(_10_)
  );
  AND _27_ (
    .A(_09_),
    .B(_10_),
    .Y(y[1])
  );
endmodule
