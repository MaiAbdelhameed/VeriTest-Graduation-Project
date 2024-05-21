/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xnor27.v:2.1-11.10" */
module xnor27(a, b, out);
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
  /* src = "xnor27.v:3.22-3.23" */
  input [7:0] a;
  wire [7:0] a;
  /* src = "xnor27.v:4.22-4.23" */
  input [7:0] b;
  wire [7:0] b;
  /* src = "xnor27.v:5.23-5.26" */
  output [7:0] out;
  wire [7:0] out;
  OR _24_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_00_)
  );
  NOT _25_ (
    .A(_00_),
    .Y(_01_)
  );
  AND _26_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_02_)
  );
  OR _27_ (
    .A(_01_),
    .B(_02_),
    .Y(out[3])
  );
  OR _28_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_03_)
  );
  NOT _29_ (
    .A(_03_),
    .Y(_04_)
  );
  AND _30_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_05_)
  );
  OR _31_ (
    .A(_04_),
    .B(_05_),
    .Y(out[4])
  );
  OR _32_ (
    .A(a[5]),
    .B(b[5]),
    .Y(_06_)
  );
  NOT _33_ (
    .A(_06_),
    .Y(_07_)
  );
  AND _34_ (
    .A(a[5]),
    .B(b[5]),
    .Y(_08_)
  );
  OR _35_ (
    .A(_07_),
    .B(_08_),
    .Y(out[5])
  );
  OR _36_ (
    .A(a[6]),
    .B(b[6]),
    .Y(_09_)
  );
  NOT _37_ (
    .A(_09_),
    .Y(_10_)
  );
  AND _38_ (
    .A(a[6]),
    .B(b[6]),
    .Y(_11_)
  );
  OR _39_ (
    .A(_10_),
    .B(_11_),
    .Y(out[6])
  );
  OR _40_ (
    .A(a[7]),
    .B(b[7]),
    .Y(_12_)
  );
  NOT _41_ (
    .A(_12_),
    .Y(_13_)
  );
  AND _42_ (
    .A(a[7]),
    .B(b[7]),
    .Y(_14_)
  );
  OR _43_ (
    .A(_13_),
    .B(_14_),
    .Y(out[7])
  );
  OR _44_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_15_)
  );
  NOT _45_ (
    .A(_15_),
    .Y(_16_)
  );
  AND _46_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_17_)
  );
  OR _47_ (
    .A(_16_),
    .B(_17_),
    .Y(out[0])
  );
  OR _48_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_18_)
  );
  NOT _49_ (
    .A(_18_),
    .Y(_19_)
  );
  AND _50_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_20_)
  );
  OR _51_ (
    .A(_19_),
    .B(_20_),
    .Y(out[1])
  );
  OR _52_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_21_)
  );
  NOT _53_ (
    .A(_21_),
    .Y(_22_)
  );
  AND _54_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_23_)
  );
  OR _55_ (
    .A(_22_),
    .B(_23_),
    .Y(out[2])
  );
endmodule
