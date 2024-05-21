// tested
module mux28(out, a, b, c, d, s0, s1);
    output out;
    input a, b, c, d, s0, s1;
    wire s0bar, s1bar, T1, T2, T3;

    not u1(s1bar, s1);
    not u2(s0bar, s0);

    assign T1 = a & s0bar & s1bar;
    assign T2 = b & s0 & s1bar;
    assign T3 = c & s0bar & s1;
    assign T4 = d & s0 & s1;

    assign out = T1 | T2 | T3 | T4;
endmodule