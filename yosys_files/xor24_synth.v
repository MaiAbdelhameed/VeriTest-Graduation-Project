/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xor24.v:2.1-10.10" */
module xor24(a, b, out);
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
  /* src = "xor24.v:3.22-3.23" */
  input [4:0] a;
  wire [4:0] a;
  /* src = "xor24.v:4.22-4.23" */
  input [4:0] b;
  wire [4:0] b;
  /* src = "xor24.v:5.23-5.26" */
  output [4:0] out;
  wire [4:0] out;
  AND _15_ (
    .A(_06_),
    .B(_08_),
    .Y(out[2])
  );
  OR _16_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_09_)
  );
  AND _17_ (
    .A(a[3]),
    .B(b[3]),
    .Y(_10_)
  );
  NOT _18_ (
    .A(_10_),
    .Y(_11_)
  );
  AND _19_ (
    .A(_09_),
    .B(_11_),
    .Y(out[3])
  );
  OR _20_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_12_)
  );
  AND _21_ (
    .A(a[4]),
    .B(b[4]),
    .Y(_13_)
  );
  NOT _22_ (
    .A(_13_),
    .Y(_14_)
  );
  AND _23_ (
    .A(_12_),
    .B(_14_),
    .Y(out[4])
  );
  OR _24_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_00_)
  );
  AND _25_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_01_)
  );
  NOT _26_ (
    .A(_01_),
    .Y(_02_)
  );
  AND _27_ (
    .A(_00_),
    .B(_02_),
    .Y(out[0])
  );
  OR _28_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_03_)
  );
  AND _29_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_04_)
  );
  NOT _30_ (
    .A(_04_),
    .Y(_05_)
  );
  AND _31_ (
    .A(_03_),
    .B(_05_),
    .Y(out[1])
  );
  OR _32_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_06_)
  );
  AND _33_ (
    .A(a[2]),
    .B(b[2]),
    .Y(_07_)
  );
  NOT _34_ (
    .A(_07_),
    .Y(_08_)
  );
endmodule
