module mult34 (input [1:0] a, b,
            output [3:0] result);

    wire [1:0] a_b_0, a_b_1;

    and gate_a0(a_b_0[0], a[0], b[0]);
    and gate_a1(a_b_1[0], a[1], b[0]);
    and gate_a2(a_b_0[1], a[0], b[1]);
    and gate_a3(a_b_1[1], a[1], b[1]);

    assign result = {a_b_0[0], a_b_0[1]} + {a_b_1[0], a_b_1[1], 2'b0};
endmodule