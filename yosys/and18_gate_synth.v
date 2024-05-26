/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "and18_gate.v:2.1-29.10" */
module and18_gate(a, b, out);
  /* src = "and18_gate.v:3.23-3.24" */
  input [15:0] a;
  wire [15:0] a;
  /* src = "and18_gate.v:4.23-4.24" */
  input [15:0] b;
  wire [15:0] b;
  /* src = "and18_gate.v:5.23-5.26" */
  output [15:0] out;
  wire [15:0] out;
  AND _00_ (
    .A(a[10]),
    .B(b[10]),
    .Y(out[10])
  );
  AND _01_ (
    .A(a[9]),
    .B(b[9]),
    .Y(out[9])
  );
  AND _02_ (
    .A(a[8]),
    .B(b[8]),
    .Y(out[8])
  );
  AND _03_ (
    .A(a[7]),
    .B(b[7]),
    .Y(out[7])
  );
  AND _04_ (
    .A(a[6]),
    .B(b[6]),
    .Y(out[6])
  );
  AND _05_ (
    .A(a[5]),
    .B(b[5]),
    .Y(out[5])
  );
  AND _06_ (
    .A(a[4]),
    .B(b[4]),
    .Y(out[4])
  );
  AND _07_ (
    .A(a[3]),
    .B(b[3]),
    .Y(out[3])
  );
  AND _08_ (
    .A(a[2]),
    .B(b[2]),
    .Y(out[2])
  );
  AND _09_ (
    .A(a[1]),
    .B(b[1]),
    .Y(out[1])
  );
  AND _10_ (
    .A(a[0]),
    .B(b[0]),
    .Y(out[0])
  );
  AND _11_ (
    .A(a[15]),
    .B(b[15]),
    .Y(out[15])
  );
  AND _12_ (
    .A(a[14]),
    .B(b[14]),
    .Y(out[14])
  );
  AND _13_ (
    .A(a[13]),
    .B(b[13]),
    .Y(out[13])
  );
  AND _14_ (
    .A(a[12]),
    .B(b[12]),
    .Y(out[12])
  );
  AND _15_ (
    .A(a[11]),
    .B(b[11]),
    .Y(out[11])
  );
endmodule