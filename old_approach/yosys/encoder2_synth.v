/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "encoder2.v:1.1-17.10" */
module encoder2(din, dout);
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
  wire _32_;
  wire _33_;
  wire _34_;
  wire _35_;
  wire _36_;
  wire _37_;
  wire _38_;
  wire _39_;
  wire _40_;
  wire _41_;
  wire _42_;
  wire _43_;
  /* src = "encoder2.v:2.13-2.16" */
  input [7:0] din;
  wire [7:0] din;
  /* src = "encoder2.v:3.14-3.18" */
  output [2:0] dout;
  wire [2:0] dout;
  not _44_ (
    .A(din[6]),
    .Y(_00_)
  );
  not _45_ (
    .A(din[5]),
    .Y(_01_)
  );
  not _46_ (
    .A(din[4]),
    .Y(_02_)
  );
  not _47_ (
    .A(din[3]),
    .Y(_03_)
  );
  not _48_ (
    .A(din[1]),
    .Y(_04_)
  );
  OR _49_ (
    .A(din[3]),
    .B(din[0]),
    .Y(_05_)
  );
  not _50_ (
    .A(_05_),
    .Y(_06_)
  );
  AND _51_ (
    .A(_04_),
    .B(_06_),
    .Y(_07_)
  );
  OR _52_ (
    .A(din[1]),
    .B(_05_),
    .Y(_08_)
  );
  OR _53_ (
    .A(din[2]),
    .B(_08_),
    .Y(_09_)
  );
  not _54_ (
    .A(_09_),
    .Y(_10_)
  );
  AND _55_ (
    .A(_01_),
    .B(_02_),
    .Y(_11_)
  );
  OR _56_ (
    .A(din[5]),
    .B(din[4]),
    .Y(_12_)
  );
  AND _57_ (
    .A(_10_),
    .B(_11_),
    .Y(_13_)
  );
  AND _58_ (
    .A(din[7]),
    .B(_00_),
    .Y(_14_)
  );
  AND _59_ (
    .A(_13_),
    .B(_14_),
    .Y(_15_)
  );
  OR _60_ (
    .A(din[7]),
    .B(din[6]),
    .Y(_16_)
  );
  not _61_ (
    .A(_16_),
    .Y(_17_)
  );
  AND _62_ (
    .A(_11_),
    .B(_17_),
    .Y(_18_)
  );
  OR _63_ (
    .A(_12_),
    .B(_16_),
    .Y(_19_)
  );
  OR _64_ (
    .A(din[2]),
    .B(_19_),
    .Y(_20_)
  );
  OR _65_ (
    .A(_04_),
    .B(_05_),
    .Y(_21_)
  );
  OR _66_ (
    .A(_20_),
    .B(_21_),
    .Y(_22_)
  );
  OR _67_ (
    .A(_03_),
    .B(din[1]),
    .Y(_23_)
  );
  OR _68_ (
    .A(din[0]),
    .B(_23_),
    .Y(_24_)
  );
  OR _69_ (
    .A(_20_),
    .B(_24_),
    .Y(_25_)
  );
  not _70_ (
    .A(_25_),
    .Y(_26_)
  );
  AND _71_ (
    .A(_22_),
    .B(_25_),
    .Y(_27_)
  );
  AND _72_ (
    .A(_10_),
    .B(_17_),
    .Y(_28_)
  );
  OR _73_ (
    .A(_09_),
    .B(_16_),
    .Y(_29_)
  );
  OR _74_ (
    .A(_01_),
    .B(din[4]),
    .Y(_30_)
  );
  OR _75_ (
    .A(_29_),
    .B(_30_),
    .Y(_31_)
  );
  AND _76_ (
    .A(_27_),
    .B(_31_),
    .Y(_32_)
  );
  not _77_ (
    .A(_32_),
    .Y(_33_)
  );
  OR _78_ (
    .A(_15_),
    .B(_33_),
    .Y(dout[0])
  );
  AND _79_ (
    .A(din[7]),
    .B(din[6]),
    .Y(_34_)
  );
  not _80_ (
    .A(_34_),
    .Y(_35_)
  );
  AND _81_ (
    .A(_16_),
    .B(_35_),
    .Y(_36_)
  );
  AND _82_ (
    .A(_13_),
    .B(_36_),
    .Y(_37_)
  );
  AND _83_ (
    .A(din[2]),
    .B(_07_),
    .Y(_38_)
  );
  AND _84_ (
    .A(_18_),
    .B(_38_),
    .Y(_39_)
  );
  OR _85_ (
    .A(_26_),
    .B(_39_),
    .Y(_40_)
  );
  OR _86_ (
    .A(_37_),
    .B(_40_),
    .Y(dout[1])
  );
  OR _87_ (
    .A(_01_),
    .B(_02_),
    .Y(_41_)
  );
  AND _88_ (
    .A(_12_),
    .B(_41_),
    .Y(_42_)
  );
  AND _89_ (
    .A(_28_),
    .B(_42_),
    .Y(_43_)
  );
  OR _90_ (
    .A(_37_),
    .B(_43_),
    .Y(dout[2])
  );
endmodule