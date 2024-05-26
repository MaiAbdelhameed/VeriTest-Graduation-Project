// tested
module xor6 (
    input [15:0] a,
    input [15:0] b,
    output [15:0] out
);

  // Instantiate an xor gate primitive
    xor (out[0], a[0], b[0]);
    xor (out[1], a[1], b[1]);
    xor (out[2], a[2], b[2]);
    xor (out[3], a[3], b[3]);
    
    xor (out[4], a[4], b[4]);
    xor (out[5], a[5], b[5]);
    xor (out[6], a[6], b[6]);
    xor (out[7], a[7], b[7]);

    xor (out[8], a[8], b[8]);
    xor (out[9], a[9], b[9]);
    xor (out[10], a[10], b[10]);
    xor (out[11], a[11], b[11]);
    
    xor (out[12], a[12], b[12]);
    xor (out[13], a[13], b[13]);
    xor (out[14], a[14], b[14]);
    xor (out[15], a[15], b[15]);

endmodule