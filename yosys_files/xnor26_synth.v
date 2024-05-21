/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xnor26.v:2.1-10.10" */
module xnor26(a, b, out);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  /* src = "xnor26.v:3.22-3.23" */
  input [1:0] a;
  wire [1:0] a;
  /* src = "xnor26.v:4.22-4.23" */
  input [1:0] b;
  wire [1:0] b;
  /* src = "xnor26.v:5.23-5.26" */
  output [1:0] out;
  wire [1:0] out;
  OR _06_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_03_)
  );
  NOT _07_ (
    .A(_03_),
    .Y(_04_)
  );
  AND _08_ (
    .A(a[0]),
    .B(b[0]),
    .Y(_05_)
  );
  OR _09_ (
    .A(_04_),
    .B(_05_),
    .Y(out[0])
  );
  OR _10_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_00_)
  );
  NOT _11_ (
    .A(_00_),
    .Y(_01_)
  );
  AND _12_ (
    .A(a[1]),
    .B(b[1]),
    .Y(_02_)
  );
  OR _13_ (
    .A(_01_),
    .B(_02_),
    .Y(out[1])
  );
endmodule