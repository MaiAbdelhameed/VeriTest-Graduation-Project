// tested
module nand31 (
    input [7:0] a,
    input [7:0] b,
    output [7:0] out
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


endmodule