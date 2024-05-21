/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* top =  1  */
/* src = "mai.v:2.1-12.10" */
module mai(a, b, product);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  /* src = "mai.v:3.17-3.18" */
  input [1:0] a;
  wire [1:0] a;
  /* src = "mai.v:4.17-4.18" */
  input [1:0] b;
  wire [1:0] b;
  /* src = "mai.v:5.22-5.29" */
  output [3:0] product;
  wire [3:0] product;
  AND _06_ (
    .A(b[0]),
    .B(a[0]),
    .Y(product[0])
  );
  NOT _07_ (
    .A(product[0]),
    .Y(_00_)
  );
  AND _08_ (
    .A(b[1]),
    .B(a[1]),
    .Y(_01_)
  );
  AND _09_ (
    .A(_00_),
    .B(_01_),
    .Y(product[2])
  );
  AND _10_ (
    .A(b[1]),
    .B(a[0]),
    .Y(_02_)
  );
  AND _11_ (
    .A(a[1]),
    .B(b[0]),
    .Y(_03_)
  );
  AND _12_ (
    .A(_02_),
    .B(_03_),
    .Y(product[3])
  );
  NOT _13_ (
    .A(product[3]),
    .Y(_04_)
  );
  OR _14_ (
    .A(_02_),
    .B(_03_),
    .Y(_05_)
  );
  AND _15_ (
    .A(_04_),
    .B(_05_),
    .Y(product[1])
  );
endmodule
