// tested
module adder20(Y,carryout,A,B,carryin);
  output [3:0]Y;
  output carryout;
  input [3:0]A,B;
  input carryin;

  wire [3:0]g,p;// generate and propogate  
  wire [4:0]c;// intermediate carry of adders, one extra for coding simplicity
  wire z;// for the mux
  
  assign c[0] = carryin; // this line is not needed can be directly written
  
    assign p[0] = A[0] ^ B[0];
    assign c[1] = ( A[0] & B[0] ) | ( A[0] & c[0] ) | ( B[0] & c[0] );
    assign Y[0] = A[0] ^ B[0] ^ c[0];

    assign p[1] = A[1] ^ B[1];
    assign c[2] = ( A[1] & B[1] ) | ( A[1] & c[1] ) | ( B[1] & c[1] );
    assign Y[1] = A[1] ^ B[1] ^ c[1];

    assign p[2] = A[2] ^ B[2];
    assign c[3] = ( A[2] & B[2] ) | ( A[2] & c[2] ) | ( B[2] & c[2] );
    assign Y[2] = A[2] ^ B[2] ^ c[2];

    assign p[3] = A[3] ^ B[3];
    assign c[4] = ( A[3] & B[3] ) | ( A[3] & c[3] ) | ( B[3] & c[3] );
    assign Y[3] = A[3] ^ B[3] ^ c[3];
  // now assign the mux value correctly
  
  assign z = p[0] & p [1] & p[2] & p[3];
  assign carryout = z ? carryin : c[4];

endmodule

/* IGNORE BELOW YA MAI, KEEP IT COMMENTED
// Second reuse the above block modules to build the final adder
// The adder is a 8 bit adder which will make use of two blocks of 4 bit each
module jcarryskipadder(Y,carryout,A,B,carryin);
  output [7:0]Y;
  output carryout;
  input [7:0]A,B;
  input carryin;

  wire c4; // intermediate carry obtained from first block
  
  //jcsablock b1 (Y[3:0],c4,A[3:0],B[3:0],carryin);
  //jcsablock b2 (Y[7:4],carryout,A[7:4],B[7:4],c4)
  wire [3:0]g0,p0;// generate and propogate  
  wire [4:0]c0;// intermediate carry of adders, one extra for coding simplicity
  wire z0;// for the mux
  
  assign c0[0] = carryin; // this line is not needed can be directly written
  
  genvar i;
  for (i=0; i<=3; i=i+1)
  begin
    assign p0[i] = A[i] ^ B[i];
    assign c0[i+1] = ( A[i] & B[i] ) | ( A[i] & c0[i] ) | ( B[i] & c0[i] );
    assign Y[i] = A[i] ^ B[i] ^ c0[i];
  end
  // now assign the mux value correctly
  
  assign z0 = p0[0] & p0 [1] & p0[2] & p0[3];
  assign c4 = z0 ? carryin : c0[4];

  wire [3:0]g,p;// generate and propogate  
  wire [4:0]c;// intermediate carry of adders, one extra for coding simplicity
  wire z;// for the mux
  
  assign c[0] = c4; // this line is not needed can be directly written
  
  genvar j;
  for (j=4; j<=7; j=j+1)
  begin
    assign p[j] = A[j] ^ B[j];
    assign c[j+1] = ( A[j] & B[j] ) | ( A[j] & c[j] ) | ( B[j] & c[j] );
    assign Y[j] = A[j] ^ B[j] ^ c[j];
  end
  // now assign the mux value correctly
  
  assign z = p[0] & p [1] & p[2] & p[3];
  assign carryout = z ? c4 : c[4];
  
endmodule

*/