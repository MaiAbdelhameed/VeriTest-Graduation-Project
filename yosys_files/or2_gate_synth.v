/* Generated by Yosys 0.41+83 (git sha1 7045cf509, x86_64-w64-mingw32-g++ 13.2.1 -Os) */

/* cells_not_processed =  1  */
/* src = "or2_gate.v:2.1-11.10" */
module or2_gate(a, b, out);
  /* src = "or2_gate.v:3.9-3.10" */
  input a;
  wire a;
  /* src = "or2_gate.v:4.9-4.10" */
  input b;
  wire b;
  /* src = "or2_gate.v:5.10-5.13" */
  output out;
  wire out;
  OR _0_ (
    .A(a),
    .B(b),
    .Y(out)
  );
endmodule
