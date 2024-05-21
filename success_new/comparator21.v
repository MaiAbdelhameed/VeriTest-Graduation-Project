module comparator21 (input a0,input a1, input b0,input b1, output eq, output gt, output lt);

    assign eq = ({a1,a0} == {b1,b0});
    assign gt = ({a1,a0} > {b1,b0});
    assign lt = ({a1,a0} < {b1,b0});

endmodule
