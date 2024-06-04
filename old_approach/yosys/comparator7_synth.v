/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "comparator7.v:1.1-15.10" */
module comparator7(a, b, eq, greater, less);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  /* src = "comparator7.v:2.11-2.12" */
  input a;
  wire a;
  /* src = "comparator7.v:3.11-3.12" */
  input b;
  wire b;
  /* src = "comparator7.v:4.16-4.18" */
  output eq;
  wire eq;
  /* src = "comparator7.v:5.16-5.23" */
  output greater;
  wire greater;
  /* src = "comparator7.v:6.16-6.20" */
  output less;
  wire less;
  not _04_ (
    .A(a),
    .Y(_01_)
  );
  not _05_ (
    .A(b),
    .Y(_02_)
  );
  OR _06_ (
    .A(a),
    .B(_02_),
    .Y(_03_)
  );
  not _07_ (
    .A(_03_),
    .Y(less)
  );
  OR _08_ (
    .A(_01_),
    .B(b),
    .Y(_00_)
  );
  not _09_ (
    .A(_00_),
    .Y(greater)
  );
  AND _10_ (
    .A(_03_),
    .B(_00_),
    .Y(eq)
  );
endmodule