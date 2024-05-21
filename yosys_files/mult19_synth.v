/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "mult19.v:1.1-15.10" */
module mult19(a, b, result);
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
  /* src = "mult19.v:2.17-2.18" */
  input [2:0] a;
  wire [2:0] a;
  /* src = "mult19.v:3.17-3.18" */
  input [1:0] b;
  wire [1:0] b;
  /* src = "mult19.v:4.22-4.28" */
  output [4:0] result;
  wire [4:0] result;
  AND _18_ (
    .A(a[1]),
    .B(b[0]),
    .Y(_00_)
  );
  AND _19_ (
    .A(b[1]),
    .B(a[0]),
    .Y(_01_)
  );
  OR _20_ (
    .A(_00_),
    .B(_01_),
    .Y(_02_)
  );
  AND _21_ (
    .A(_00_),
    .B(_01_),
    .Y(_03_)
  );
  NOT _22_ (
    .A(_03_),
    .Y(_04_)
  );
  AND _23_ (
    .A(_02_),
    .B(_04_),
    .Y(result[1])
  );
  AND _24_ (
    .A(b[0]),
    .B(a[0]),
    .Y(result[0])
  );
  NOT _25_ (
    .A(result[0]),
    .Y(_05_)
  );
  OR _26_ (
    .A(a[2]),
    .B(_05_),
    .Y(_06_)
  );
  AND _27_ (
    .A(b[0]),
    .B(a[2]),
    .Y(_07_)
  );
  AND _28_ (
    .A(a[2]),
    .B(_00_),
    .Y(_08_)
  );
  NOT _29_ (
    .A(_08_),
    .Y(_09_)
  );
  AND _30_ (
    .A(a[1]),
    .B(_06_),
    .Y(_10_)
  );
  AND _31_ (
    .A(b[1]),
    .B(_09_),
    .Y(_11_)
  );
  OR _32_ (
    .A(_01_),
    .B(_11_),
    .Y(_12_)
  );
  AND _33_ (
    .A(_10_),
    .B(_12_),
    .Y(_13_)
  );
  AND _34_ (
    .A(b[1]),
    .B(_08_),
    .Y(result[4])
  );
  NOT _35_ (
    .A(result[4]),
    .Y(_14_)
  );
  AND _36_ (
    .A(_07_),
    .B(_14_),
    .Y(_15_)
  );
  OR _37_ (
    .A(_13_),
    .B(_15_),
    .Y(result[2])
  );
  AND _38_ (
    .A(a[1]),
    .B(result[0]),
    .Y(_16_)
  );
  OR _39_ (
    .A(a[2]),
    .B(_16_),
    .Y(_17_)
  );
  AND _40_ (
    .A(_11_),
    .B(_17_),
    .Y(result[3])
  );
endmodule
