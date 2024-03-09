module comparator24 (input a, input b, output reg eq, output reg gt, output reg lt);

    reg a_xor_b, a_and_b;
    reg a_nor_b;

    integer i;
    always @* begin
        for (i = 0; i < 2; i = i + 1) begin
            case(i)
                0: a_xor_b = a ^ b;
                1: a_and_b = a & b;
                2: a_nor_b = ~(a | b);
            endcase
        end
    end

    assign eq = ~a_nor_b;
    assign gt = a_and_b;
    assign lt = a_xor_b;

endmodule
