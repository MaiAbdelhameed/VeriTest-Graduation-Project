module comparator1bit_basic_structural(input a, input b, output reg eq, output reg gt, output reg lt);

    wire w1, w1, w3;


    and u_and(w2, ~a, b); // A < B
    and u_and(w3, a, ~b); // A > B
    or u_or(w1, w2, w3); // A != B

    assign eq = ~w1;
    assign lt = w2;
    assign gt = w3;

endmodule
