/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "xor26.v:1.1-12.10" */
module xor26(a, b, c, d, e, out);
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
  wire _18_;
  wire _19_;
  wire _20_;
  /* src = "xor26.v:2.16-2.17" */
  input a;
  wire a;
  /* src = "xor26.v:3.16-3.17" */
  input b;
  wire b;
  /* src = "xor26.v:4.16-4.17" */
  input c;
  wire c;
  /* src = "xor26.v:5.16-5.17" */
  input d;
  wire d;
  /* src = "xor26.v:6.16-6.17" */
  input e;
  wire e;
  /* src = "xor26.v:7.17-7.20" */
  output out;
  wire out;
  OR _21_ (
    .A(d),
    .B(e),
    .Y(_10_)
  );
  NOT _22_ (
    .A(_10_),
    .Y(_11_)
  );
  AND _23_ (
    .A(d),
    .B(e),
    .Y(_12_)
  );
  NOT _24_ (
    .A(_12_),
    .Y(_13_)
  );
  AND _25_ (
    .A(_10_),
    .B(_13_),
    .Y(_14_)
  );
  OR _26_ (
    .A(_11_),
    .B(_12_),
    .Y(_15_)
  );
  OR _27_ (
    .A(_08_),
    .B(_15_),
    .Y(_16_)
  );
  OR _28_ (
    .A(_09_),
    .B(_14_),
    .Y(_17_)
  );
  AND _29_ (
    .A(_16_),
    .B(_17_),
    .Y(out)
  );
  NOT _30_ (
    .A(c),
    .Y(_18_)
  );
  AND _31_ (
    .A(a),
    .B(b),
    .Y(_19_)
  );
  NOT _32_ (
    .A(_19_),
    .Y(_20_)
  );
  OR _33_ (
    .A(a),
    .B(b),
    .Y(_00_)
  );
  NOT _34_ (
    .A(_00_),
    .Y(_01_)
  );
  OR _35_ (
    .A(_19_),
    .B(_01_),
    .Y(_02_)
  );
  AND _36_ (
    .A(_20_),
    .B(_00_),
    .Y(_03_)
  );
  AND _37_ (
    .A(c),
    .B(_02_),
    .Y(_04_)
  );
  OR _38_ (
    .A(_18_),
    .B(_03_),
    .Y(_05_)
  );
  AND _39_ (
    .A(_18_),
    .B(_03_),
    .Y(_06_)
  );
  OR _40_ (
    .A(c),
    .B(_02_),
    .Y(_07_)
  );
  AND _41_ (
    .A(_05_),
    .B(_07_),
    .Y(_08_)
  );
  OR _42_ (
    .A(_04_),
    .B(_06_),
    .Y(_09_)
  );
endmodule