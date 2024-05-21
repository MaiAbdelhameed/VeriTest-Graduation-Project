/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "decoder2.v:2.1-18.10" */
module decoder2(en, a, b, y);
  /* src = "decoder2.v:6.5-17.8" */
  wire [3:0] _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  /* src = "decoder2.v:3.14-3.15" */
  input a;
  wire a;
  /* src = "decoder2.v:3.16-3.17" */
  input b;
  wire b;
  /* src = "decoder2.v:3.11-3.13" */
  input en;
  wire en;
  /* src = "decoder2.v:4.21-4.22" */
  output [3:0] y;
  reg [3:0] y;
  NOT _05_ (
    .A(b),
    .Y(_01_)
  );
  NOT _06_ (
    .A(a),
    .Y(_02_)
  );
  OR _07_ (
    .A(b),
    .B(en),
    .Y(_03_)
  );
  OR _08_ (
    .A(a),
    .B(_03_),
    .Y(_00_[0])
  );
  OR _09_ (
    .A(_01_),
    .B(en),
    .Y(_04_)
  );
  OR _10_ (
    .A(a),
    .B(_04_),
    .Y(_00_[1])
  );
  OR _11_ (
    .A(_02_),
    .B(_03_),
    .Y(_00_[2])
  );
  OR _12_ (
    .A(_02_),
    .B(_04_),
    .Y(_00_[3])
  );
  /* src = "decoder2.v:6.5-17.8" */
  always @*
    if (!1'h0) y[0] = _00_[0];
  /* src = "decoder2.v:6.5-17.8" */
  always @*
    if (!1'h0) y[1] = _00_[1];
  /* src = "decoder2.v:6.5-17.8" */
  always @*
    if (!1'h0) y[2] = _00_[2];
  /* src = "decoder2.v:6.5-17.8" */
  always @*
    if (!1'h0) y[3] = _00_[3];
endmodule
