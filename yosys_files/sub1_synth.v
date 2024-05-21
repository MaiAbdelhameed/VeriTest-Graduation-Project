/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "sub1.v:2.1-10.10" */
module sub1(a, b, c, sum, cout);
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
  /* src = "sub1.v:4.8-4.9" */
  input a;
  wire a;
  /* src = "sub1.v:4.10-4.11" */
  input b;
  wire b;
  /* src = "sub1.v:4.12-4.13" */
  input c;
  wire c;
  /* src = "sub1.v:5.14-5.18" */
  output cout;
  wire cout;
  /* src = "sub1.v:5.9-5.12" */
  output sum;
  wire sum;
  OR _12_ (
    .A(_08_),
    .B(b),
    .Y(_02_)
  );
  AND _13_ (
    .A(_00_),
    .B(_02_),
    .Y(_03_)
  );
  OR _14_ (
    .A(_11_),
    .B(_01_),
    .Y(_04_)
  );
  OR _15_ (
    .A(_10_),
    .B(_03_),
    .Y(_05_)
  );
  OR _16_ (
    .A(c),
    .B(_04_),
    .Y(_06_)
  );
  AND _17_ (
    .A(_05_),
    .B(_06_),
    .Y(sum)
  );
  OR _18_ (
    .A(c),
    .B(_11_),
    .Y(_07_)
  );
  AND _19_ (
    .A(_02_),
    .B(_07_),
    .Y(cout)
  );
  NOT _20_ (
    .A(a),
    .Y(_08_)
  );
  NOT _21_ (
    .A(b),
    .Y(_09_)
  );
  NOT _22_ (
    .A(c),
    .Y(_10_)
  );
  AND _23_ (
    .A(_08_),
    .B(b),
    .Y(_11_)
  );
  OR _24_ (
    .A(a),
    .B(_09_),
    .Y(_00_)
  );
  AND _25_ (
    .A(a),
    .B(_09_),
    .Y(_01_)
  );
endmodule
