module comparator21 (input a, input b, output eq, output gt, output lt);

    assign eq = (a == b);
    assign gt = (a > b);
    assign lt = (a < b);

endmodule
