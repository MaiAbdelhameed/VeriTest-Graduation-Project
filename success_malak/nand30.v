// tested
module nand30 (
    input [15:0] a,
    input [15:0] b,
    output [15:0] out
);

  // Instantiate an OR gate primitive
    or (out[0], ~a[0], ~b[0]);
    or (out[1], ~a[1], ~b[1]);
    or (out[2], ~a[2], ~b[2]);
    or (out[3], ~a[3], ~b[3]);
    
    or (out[4], ~a[4], ~b[4]);
    or (out[5], ~a[5], ~b[5]);
    or (out[6], ~a[6], ~b[6]);
    or (out[7], ~a[7], ~b[7]);

    or (out[8], ~a[8], ~b[8]);
    or (out[9], ~a[9], ~b[9]);
    or (out[10], ~a[10], ~b[10]);
    or (out[11], ~a[11], ~b[11]);
    
    or (out[12], ~a[12], ~b[12]);
    or (out[13], ~a[13], ~b[13]);
    or (out[14], ~a[14], ~b[14]);
    or (out[15], ~a[15], ~b[15]);

endmodule