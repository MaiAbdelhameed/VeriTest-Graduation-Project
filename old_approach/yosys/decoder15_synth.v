/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "decoder15.v:1.1-21.10" */
module decoder15(in, en, out);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  /* src = "decoder15.v:4.11-4.13" */
  input en;
  wire en;
  /* src = "decoder15.v:3.14-3.16" */
  input [1:0] in;
  wire [1:0] in;
  /* src = "decoder15.v:5.19-5.22" */
  output [3:0] out;
  wire [3:0] out;
  not _05_ (
    .A(in[1]),
    .Y(_03_)
  );
  not _06_ (
    .A(in[0]),
    .Y(_04_)
  );
  AND _07_ (
    .A(in[1]),
    .B(en),
    .Y(_00_)
  );
  AND _08_ (
    .A(in[0]),
    .B(_00_),
    .Y(out[0])
  );
  AND _09_ (
    .A(_04_),
    .B(_00_),
    .Y(out[1])
  );
  AND _10_ (
    .A(in[0]),
    .B(en),
    .Y(_01_)
  );
  AND _11_ (
    .A(_03_),
    .B(_01_),
    .Y(out[2])
  );
  AND _12_ (
    .A(_03_),
    .B(_04_),
    .Y(_02_)
  );
  AND _13_ (
    .A(en),
    .B(_02_),
    .Y(out[3])
  );
endmodule