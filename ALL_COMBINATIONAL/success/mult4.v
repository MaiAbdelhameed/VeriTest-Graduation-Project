module mult4 (input [1:0] a, b,
            output [3:0] result);

    wire a0b0, a0b1, a1b0, a1b1;

    and gate_a0(a0b0, a[0], b[0]);
    and gate_a1(a1b0, a[1], b[0]);
    and gate_a2(a0b1, a[0], b[1]);
    and gate_a3(a1b1, a[1], b[1]);

    assign result = {a1b0,a0b0} + {a1b1,a0b1,1'b0};
endmodule