module mult5 (input a1,a0,b1,b0,
            output [3:0] result);

    wire a0b0, a0b1, a1b0, a1b1;

    and gate_a0(a0b0, a0, b0);
    and gate_a1(a1b0, a1, b0);
    and gate_a2(a0b1, a0, b1);
    and gate_a3(a1b1, a1, b1);

    assign result = {a1b0,a0b0} + {a1b1,a0b1,1'b0};
endmodule