/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xor18.v:2.1-20.10" */
module xor18(a, b, out);
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
  /* src = "xor18.v:3.22-3.23" */
  input [5:0] a;
  wire [5:0] a;
  /* src = "xor18.v:4.22-4.23" */
  input [5:0] b;
  wire [5:0] b;
  /* src = "xor18.v:5.22-5.25" */
  output [5:0] out;
  wire [5:0] out;
  OR _18_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_06_)
  );
  AND _19_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_07_)
  );
  not _20_ (
    .A(_07_),
    .Y(_08_)
  );
  AND _21_ (
    .A(_06_),
    .B(_08_),
    .Y(out[3])
  );
  OR _22_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_09_)
  );
  AND _23_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_10_)
  );
  not _24_ (
    .A(_10_),
    .Y(_11_)
  );
  AND _25_ (
    .A(_09_),
    .B(_11_),
    .Y(out[2])
  );
  OR _26_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_12_)
  );
  AND _27_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_13_)
  );
  not _28_ (
    .A(_13_),
    .Y(_14_)
  );
  AND _29_ (
    .A(_12_),
    .B(_14_),
    .Y(out[1])
  );
  OR _30_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_15_)
  );
  AND _31_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_16_)
  );
  not _32_ (
    .A(_16_),
    .Y(_17_)
  );
  AND _33_ (
    .A(_15_),
    .B(_17_),
    .Y(out[0])
  );
  OR _34_ (
    .A(a[5]),
    .B(b[5]),
    .Y(_00_)
  );
  AND _35_ (
    .A(a[5]),
    .B(b[5]),
    .Y(_01_)
  );
  not _36_ (
    .A(_01_),
    .Y(_02_)
  );
  AND _37_ (
    .A(_00_),
    .B(_02_),
    .Y(out[5])
  );
  OR _38_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_03_)
  );
  AND _39_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_04_)
  );
  not _40_ (
    .A(_04_),
    .Y(_05_)
  );
  AND _41_ (
    .A(_03_),
    .B(_05_),
    .Y(out[4])
  );
endmodule