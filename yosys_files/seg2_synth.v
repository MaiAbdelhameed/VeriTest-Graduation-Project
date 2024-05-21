/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "seg2.v:1.1-26.14" */
module seg2(bcd, seg);
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
  /* src = "seg2.v:6.17-6.20" */
  input [3:0] bcd;
  wire [3:0] bcd;
  /* src = "seg2.v:7.17-7.20" */
  output [7:0] seg;
  wire [7:0] seg;
  NOT _23_ (
    .A(bcd[0]),
    .Y(_00_)
  );
  NOT _24_ (
    .A(bcd[2]),
    .Y(_01_)
  );
  NOT _25_ (
    .A(bcd[1]),
    .Y(_02_)
  );
  NOT _26_ (
    .A(bcd[3]),
    .Y(_03_)
  );
  AND _27_ (
    .A(_01_),
    .B(_03_),
    .Y(_04_)
  );
  OR _28_ (
    .A(bcd[2]),
    .B(bcd[1]),
    .Y(_05_)
  );
  AND _29_ (
    .A(_02_),
    .B(_04_),
    .Y(_06_)
  );
  OR _30_ (
    .A(bcd[3]),
    .B(_05_),
    .Y(_07_)
  );
  AND _31_ (
    .A(bcd[0]),
    .B(_07_),
    .Y(_08_)
  );
  NOT _32_ (
    .A(_08_),
    .Y(_09_)
  );
  AND _33_ (
    .A(bcd[2]),
    .B(_03_),
    .Y(_10_)
  );
  AND _34_ (
    .A(_02_),
    .B(_10_),
    .Y(_11_)
  );
  OR _35_ (
    .A(bcd[0]),
    .B(_11_),
    .Y(_12_)
  );
  AND _36_ (
    .A(_09_),
    .B(_12_),
    .Y(seg[0])
  );
  AND _37_ (
    .A(bcd[1]),
    .B(_03_),
    .Y(_13_)
  );
  AND _38_ (
    .A(bcd[2]),
    .B(_13_),
    .Y(_14_)
  );
  AND _39_ (
    .A(_00_),
    .B(_14_),
    .Y(_15_)
  );
  AND _40_ (
    .A(bcd[0]),
    .B(_11_),
    .Y(_16_)
  );
  OR _41_ (
    .A(_15_),
    .B(_16_),
    .Y(seg[1])
  );
  AND _42_ (
    .A(bcd[1]),
    .B(_04_),
    .Y(_17_)
  );
  AND _43_ (
    .A(_00_),
    .B(_17_),
    .Y(seg[2])
  );
  AND _44_ (
    .A(bcd[0]),
    .B(_14_),
    .Y(_18_)
  );
  OR _45_ (
    .A(seg[0]),
    .B(_18_),
    .Y(seg[3])
  );
  AND _46_ (
    .A(bcd[3]),
    .B(_05_),
    .Y(_19_)
  );
  NOT _47_ (
    .A(_19_),
    .Y(_20_)
  );
  AND _48_ (
    .A(_12_),
    .B(_20_),
    .Y(seg[4])
  );
  OR _49_ (
    .A(bcd[0]),
    .B(_17_),
    .Y(_21_)
  );
  OR _50_ (
    .A(_04_),
    .B(_13_),
    .Y(_22_)
  );
  AND _51_ (
    .A(_21_),
    .B(_22_),
    .Y(seg[5])
  );
  OR _52_ (
    .A(_06_),
    .B(_18_),
    .Y(seg[6])
  );
  assign seg[7] = 1'h1;
endmodule