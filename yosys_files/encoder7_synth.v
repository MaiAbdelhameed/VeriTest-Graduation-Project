/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "encoder7.v:1.1-8.10" */
module encoder7(y, a);
  /* src = "encoder7.v:3.18-3.19" */
  output [1:0] a;
  wire [1:0] a;
  /* src = "encoder7.v:2.17-2.18" */
  input [3:0] y;
  wire [3:0] y;
  OR _0_ (
    .A(y[3]),
    .B(y[1]),
    .Y(a[0])
  );
  OR _1_ (
    .A(y[3]),
    .B(y[2]),
    .Y(a[1])
  );
endmodule
