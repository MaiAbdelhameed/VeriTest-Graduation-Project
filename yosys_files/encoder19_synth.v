/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "encoder19.v:1.1-10.10" */
module encoder19(en, D1, D2, D3, D4, D5, D6, D7, y0, y1, y2);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  /* src = "encoder19.v:4.10-4.12" */
  input D1;
  wire D1;
  /* src = "encoder19.v:4.13-4.15" */
  input D2;
  wire D2;
  /* src = "encoder19.v:4.16-4.18" */
  input D3;
  wire D3;
  /* src = "encoder19.v:4.19-4.21" */
  input D4;
  wire D4;
  /* src = "encoder19.v:4.22-4.24" */
  input D5;
  wire D5;
  /* src = "encoder19.v:4.25-4.27" */
  input D6;
  wire D6;
  /* src = "encoder19.v:4.28-4.30" */
  input D7;
  wire D7;
  /* src = "encoder19.v:4.7-4.9" */
  input en;
  wire en;
  /* src = "encoder19.v:5.8-5.10" */
  output y0;
  wire y0;
  /* src = "encoder19.v:5.11-5.13" */
  output y1;
  wire y1;
  /* src = "encoder19.v:5.14-5.16" */
  output y2;
  wire y2;
  OR _08_ (
    .A(D5),
    .B(D3),
    .Y(_00_)
  );
  OR _09_ (
    .A(D7),
    .B(D1),
    .Y(_01_)
  );
  OR _10_ (
    .A(_00_),
    .B(_01_),
    .Y(_02_)
  );
  AND _11_ (
    .A(en),
    .B(_02_),
    .Y(y0)
  );
  OR _12_ (
    .A(D7),
    .B(D6),
    .Y(_03_)
  );
  OR _13_ (
    .A(D4),
    .B(D5),
    .Y(_04_)
  );
  OR _14_ (
    .A(_03_),
    .B(_04_),
    .Y(_05_)
  );
  AND _15_ (
    .A(en),
    .B(_05_),
    .Y(y2)
  );
  OR _16_ (
    .A(D2),
    .B(D3),
    .Y(_06_)
  );
  OR _17_ (
    .A(_03_),
    .B(_06_),
    .Y(_07_)
  );
  AND _18_ (
    .A(en),
    .B(_07_),
    .Y(y1)
  );
endmodule
