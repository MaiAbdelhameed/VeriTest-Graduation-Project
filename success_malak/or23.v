//explicit gates
module or23 (
    input [15:0] a,
    input [15:0] b,
    output [15:0] out
);

  // Instantiate an OR gate primitive
    nand (out[0], ~a[0], ~b[0]);
    nand (out[1], ~a[1], ~b[1]);
    nand (out[2], ~a[2], ~b[2]);
    nand (out[3], ~a[3], ~b[3]);
    
    nand (out[4], ~a[4], ~b[4]);
    nand (out[5], ~a[5], ~b[5]);
    nand (out[6], ~a[6], ~b[6]);
    nand (out[7], ~a[7], ~b[7]);

    nand (out[8], ~a[8], ~b[8]);
    nand (out[9], ~a[9], ~b[9]);
    nand (out[10], ~a[10], ~b[10]);
    nand (out[11], ~a[11], ~b[11]);
    
    nand (out[12], ~a[12], ~b[12]);
    nand (out[13], ~a[13], ~b[13]);
    nand (out[14], ~a[14], ~b[14]);
    nand (out[15], ~a[15], ~b[15]);

endmodule