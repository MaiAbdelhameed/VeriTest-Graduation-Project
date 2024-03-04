module comparator25 (input [1:0] a, input [1:0] b, output reg eq, output reg gt, output reg lt);

    wire [1:0] a_xor_b, a_and_b;
    wire [1:0] a_nor_b;

    xor u_xor(a_xor_b, a, b);
    and u_and(a_and_b, a, b);
    nor u_nor(a_nor_b, a, b);

    assign eq = ~(a_nor_b[0] | a_nor_b[1]);
    assign gt = a_and_b[0] | (a_nor_b[1] & ~a_nor_b[0]);
    assign lt = a_xor_b[0] | (a_nor_b[0] & ~a_nor_b[1]);

endmodule

