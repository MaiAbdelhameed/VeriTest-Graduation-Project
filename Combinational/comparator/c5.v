module comparator1bit_basic_dataflow(input a, input b, output reg eq, output reg gt, output reg lt);

    always @(*) begin
        eq = (a == b);
        gt = (a > b);
        lt = (a < b);
    end

endmodule
