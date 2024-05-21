/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xor19.v:2.1-20.10" */
module xor19(a, b, out);
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
  /* src = "xor19.v:3.22-3.23" */
  input [4:0] a;
  wire [4:0] a;
  /* src = "xor19.v:4.22-4.23" */
  input [4:0] b;
  wire [4:0] b;
  /* src = "xor19.v:5.22-5.25" */
  output [4:0] out;
  wire [4:0] out;
  NOT _15_ (
    .A(_07_),
    .Y(_08_)
  );
  AND _16_ (
    .A(_06_),
    .B(_08_),
    .Y(out[2])
  );
  OR _17_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_09_)
  );
  AND _18_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_10_)
  );
  NOT _19_ (
    .A(_10_),
    .Y(_11_)
  );
  AND _20_ (
    .A(_09_),
    .B(_11_),
    .Y(out[1])
  );
  OR _21_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_12_)
  );
  AND _22_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_13_)
  );
  NOT _23_ (
    .A(_13_),
    .Y(_14_)
  );
  AND _24_ (
    .A(_12_),
    .B(_14_),
    .Y(out[0])
  );
  OR _25_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_00_)
  );
  AND _26_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_01_)
  );
  NOT _27_ (
    .A(_01_),
    .Y(_02_)
  );
  AND _28_ (
    .A(_00_),
    .B(_02_),
    .Y(out[4])
  );
  OR _29_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_03_)
  );
  AND _30_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_04_)
  );
  NOT _31_ (
    .A(_04_),
    .Y(_05_)
  );
  AND _32_ (
    .A(_03_),
    .B(_05_),
    .Y(out[3])
  );
  OR _33_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_06_)
  );
  AND _34_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_07_)
  );
endmodule
