module comparator22 (input a, input b, output eq, output gt, output lt);

    wire w1,w2,w3;

    xor u_xor(w1, a, b); // A != B
    and u_and(w2, a, ~b); // A > B
    nor u_nor(w3, ~a, b); // A < B

    assign eq = ~w1;
    assign gt = w2;
    assign lt = w3;

endmodule
