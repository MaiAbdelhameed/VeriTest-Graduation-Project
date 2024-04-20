//////////////CHECK///////////////////
module comparator19 (input a, input b, output eq, output gt, output lt);

    wire a_xor_b, a_and_b;
    wire a_nor_b;

    xor u_xor(a_xor_b, a, b);
    and u_and(a_and_b, a, b);
    nor u_nor(a_nor_b, a, b);

    assign eq = ~a_nor_b;
    assign gt = a_and_b;
    assign lt = a_xor_b;

endmodule


