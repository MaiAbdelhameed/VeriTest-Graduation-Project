//explicit gates
module or19 (
    input a,
    input b,
    output out
);

    wire Not_a,Not_b;

  // Instantiate an OR gate primitive
    not (Not_a, a);
    not (Not_b, b);
    nand (out, Not_a, Not_b);
    

endmodule