module comparator1bit_basic_dataflow(input a, input b, output eq, output gt, output lt);

    assign eq = (a == b);
    assign gt = (a > b);
    assign lt = (a < b);

endmodule
