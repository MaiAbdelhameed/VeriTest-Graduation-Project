/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "seg6.v:2.1-38.10" */
module seg6(bcd, a, b, c, d, e, f, g);
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
  wire _13_;
  wire _14_;
  wire _15_;
  wire _16_;
  wire _17_;
  wire _18_;
  wire _19_;
  wire _20_;
  wire _21_;
  wire _22_;
  wire _23_;
  wire _24_;
  wire _25_;
  wire _26_;
  wire _27_;
  wire _28_;
  wire _29_;
  wire _30_;
  wire _31_;
  /* src = "seg6.v:9.16-9.17" */
  output a;
  wire a;
  /* src = "seg6.v:9.18-9.19" */
  output b;
  wire b;
  /* src = "seg6.v:8.17-8.20" */
  input [3:0] bcd;
  wire [3:0] bcd;
  /* src = "seg6.v:9.20-9.21" */
  output c;
  wire c;
  /* src = "seg6.v:9.22-9.23" */
  output d;
  wire d;
  /* src = "seg6.v:9.24-9.25" */
  output e;
  wire e;
  /* src = "seg6.v:9.26-9.27" */
  output f;
  wire f;
  /* src = "seg6.v:9.28-9.29" */
  output g;
  wire g;
  NOT _32_ (
    .A(bcd[3]),
    .Y(_00_)
  );
  NOT _33_ (
    .A(bcd[2]),
    .Y(_01_)
  );
  NOT _34_ (
    .A(bcd[1]),
    .Y(_02_)
  );
  NOT _35_ (
    .A(bcd[0]),
    .Y(_03_)
  );
  AND _36_ (
    .A(_01_),
    .B(_02_),
    .Y(_04_)
  );
  AND _37_ (
    .A(bcd[3]),
    .B(_04_),
    .Y(_05_)
  );
  OR _38_ (
    .A(bcd[1]),
    .B(bcd[0]),
    .Y(_06_)
  );
  NOT _39_ (
    .A(_06_),
    .Y(_07_)
  );
  OR _40_ (
    .A(bcd[3]),
    .B(_06_),
    .Y(_08_)
  );
  NOT _41_ (
    .A(_08_),
    .Y(_09_)
  );
  OR _42_ (
    .A(_05_),
    .B(_09_),
    .Y(_10_)
  );
  AND _43_ (
    .A(_00_),
    .B(bcd[2]),
    .Y(_11_)
  );
  AND _44_ (
    .A(bcd[1]),
    .B(bcd[0]),
    .Y(_12_)
  );
  NOT _45_ (
    .A(_12_),
    .Y(_13_)
  );
  AND _46_ (
    .A(_06_),
    .B(_13_),
    .Y(_14_)
  );
  AND _47_ (
    .A(_11_),
    .B(_14_),
    .Y(_15_)
  );
  OR _48_ (
    .A(_10_),
    .B(_15_),
    .Y(f)
  );
  AND _49_ (
    .A(_00_),
    .B(bcd[1]),
    .Y(_16_)
  );
  AND _50_ (
    .A(_01_),
    .B(_16_),
    .Y(_17_)
  );
  OR _51_ (
    .A(_05_),
    .B(_17_),
    .Y(_18_)
  );
  OR _52_ (
    .A(_15_),
    .B(_18_),
    .Y(_19_)
  );
  AND _53_ (
    .A(_07_),
    .B(_11_),
    .Y(_20_)
  );
  OR _54_ (
    .A(_19_),
    .B(_20_),
    .Y(g)
  );
  OR _55_ (
    .A(_04_),
    .B(_16_),
    .Y(_21_)
  );
  AND _56_ (
    .A(_03_),
    .B(_21_),
    .Y(e)
  );
  OR _57_ (
    .A(bcd[2]),
    .B(_08_),
    .Y(_22_)
  );
  NOT _58_ (
    .A(_22_),
    .Y(_23_)
  );
  OR _59_ (
    .A(_19_),
    .B(_23_),
    .Y(d)
  );
  AND _60_ (
    .A(_00_),
    .B(bcd[0]),
    .Y(_24_)
  );
  OR _61_ (
    .A(bcd[3]),
    .B(_03_),
    .Y(_25_)
  );
  OR _62_ (
    .A(_11_),
    .B(_24_),
    .Y(_26_)
  );
  OR _63_ (
    .A(_04_),
    .B(_26_),
    .Y(c)
  );
  OR _64_ (
    .A(_01_),
    .B(_12_),
    .Y(_27_)
  );
  AND _65_ (
    .A(_00_),
    .B(_27_),
    .Y(_28_)
  );
  OR _66_ (
    .A(_10_),
    .B(_28_),
    .Y(b)
  );
  AND _67_ (
    .A(_04_),
    .B(_25_),
    .Y(_29_)
  );
  AND _68_ (
    .A(bcd[0]),
    .B(_11_),
    .Y(_30_)
  );
  OR _69_ (
    .A(_16_),
    .B(_29_),
    .Y(_31_)
  );
  OR _70_ (
    .A(_30_),
    .B(_31_),
    .Y(a)
  );
endmodule
