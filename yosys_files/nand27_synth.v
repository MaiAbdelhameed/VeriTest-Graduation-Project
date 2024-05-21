/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "nand27.v:3.1-17.10" */
module nand27(a, b, c, d, e, f, g, h, out);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  /* src = "nand27.v:4.9-4.10" */
  input a;
  wire a;
  /* src = "nand27.v:5.9-5.10" */
  input b;
  wire b;
  /* src = "nand27.v:6.9-6.10" */
  input c;
  wire c;
  /* src = "nand27.v:7.9-7.10" */
  input d;
  wire d;
  /* src = "nand27.v:8.9-8.10" */
  input e;
  wire e;
  /* src = "nand27.v:9.9-9.10" */
  input f;
  wire f;
  /* src = "nand27.v:10.9-10.10" */
  input g;
  wire g;
  /* src = "nand27.v:11.9-11.10" */
  input h;
  wire h;
  /* src = "nand27.v:12.10-12.13" */
  output out;
  wire out;
  AND _07_ (
    .A(e),
    .B(f),
    .Y(_00_)
  );
  AND _08_ (
    .A(g),
    .B(h),
    .Y(_01_)
  );
  AND _09_ (
    .A(_00_),
    .B(_01_),
    .Y(_02_)
  );
  AND _10_ (
    .A(a),
    .B(b),
    .Y(_03_)
  );
  AND _11_ (
    .A(c),
    .B(d),
    .Y(_04_)
  );
  AND _12_ (
    .A(_03_),
    .B(_04_),
    .Y(_05_)
  );
  AND _13_ (
    .A(_02_),
    .B(_05_),
    .Y(_06_)
  );
  NOT _14_ (
    .A(_06_),
    .Y(out)
  );
endmodule
