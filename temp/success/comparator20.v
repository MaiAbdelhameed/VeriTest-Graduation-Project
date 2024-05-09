module comparator20 (input a, input b, output eq, output gt, output lt);

    wire w1, w2, w3;


    and (w2, ~a, b); // A < B
    and (w3, a, ~b); // A > B
    or (w1, w2, w3); // A != B

    assign eq = ~w1;
    assign lt = w2;
    assign gt = w3;

endmodule