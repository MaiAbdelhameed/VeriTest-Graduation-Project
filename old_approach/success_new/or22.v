//explicit gates
module or22 (
    input [3:0] a,
    input [3:0] b,
    output [3:0] out
);

  // Instantiate an OR gate primitive
    nand (out[0], ~a[0], ~b[0]);
    nand (out[1], ~a[1], ~b[1]);
    nand (out[2], ~a[2], ~b[2]);
    nand (out[3], ~a[3], ~b[3]);
    

endmodule