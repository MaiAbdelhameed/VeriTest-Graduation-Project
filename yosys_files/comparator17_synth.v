/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "comparator17.v:1.1-10.10" */
module comparator17(a, b, L, E, G);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  /* src = "comparator17.v:3.11-3.12" */
  output E;
  wire E;
  /* src = "comparator17.v:3.14-3.15" */
  output G;
  wire G;
  /* src = "comparator17.v:3.8-3.9" */
  output L;
  wire L;
  /* src = "comparator17.v:2.7-2.8" */
  input a;
  wire a;
  /* src = "comparator17.v:2.10-2.11" */
  input b;
  wire b;
  NOT _04_ (
    .A(a),
    .Y(_01_)
  );
  NOT _05_ (
    .A(b),
    .Y(_02_)
  );
  OR _06_ (
    .A(a),
    .B(_02_),
    .Y(_03_)
  );
  NOT _07_ (
    .A(_03_),
    .Y(L)
  );
  OR _08_ (
    .A(_01_),
    .B(b),
    .Y(_00_)
  );
  NOT _09_ (
    .A(_00_),
    .Y(G)
  );
  AND _10_ (
    .A(_03_),
    .B(_00_),
    .Y(E)
  );
endmodule
