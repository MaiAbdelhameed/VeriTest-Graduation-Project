module mult36 (
  input [1:0] a,
  input [1:0] b,
  output [3:0] product
);

  wire [1:0] ab0, ab1, a0b, a1b;

  // AND gates for partial products
  and and00 (ab0[0], a[0], b[0]);
  and and01 (ab0[1], a[0], b[1]);
  and and10 (a0b[0], a[1], b[0]);
  and and11 (a1b[0], a[1], b[1]);

  // Full adders for ripple adder
  wire [2:0] sum0, sum1, sum2, sum3;
  wire cout0, cout1, cout2;

  // Full adder implementation
  assign sum0[0] = a[0] ^ b[0] ^ 0;
  assign cout0 = (a[0] & b[0]) | (b[0] & 0) | (a[0] & 0);
  assign sum0[1] = cout0;
  assign sum0[2] = 0;

  assign sum1[0] = ab0[0] ^ ab0[1] ^ sum0[0];
  assign cout1 = (ab0[0] & ab0[1]) | (ab0[1] & sum0[0]) | (ab0[0] & sum0[0]);
  assign sum1[1] = cout1;
  assign sum1[2] = 0;

  assign sum2[0] = a0b[0] ^ ab1[0] ^ sum1[0];
  assign cout2 = (a0b[0] & ab1[0]) | (ab1[0] & sum1[0]) | (a0b[0] & sum1[0]);
  assign sum2[1] = cout2;
  assign sum2[2] = 0;

  assign sum3[0] = a1b[0] ^ ab1[1] ^ sum2[0];
  assign sum3[1] = 0;
  assign sum3[2] = 0;

  // Assign outputs
  assign product[0] = sum0[0];
  assign product[1] = sum1[0];
  assign product[2] = sum2[0];
  assign product[3] = sum3[0];

endmodule
