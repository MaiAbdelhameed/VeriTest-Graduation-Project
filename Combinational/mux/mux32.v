module mux32(input [1:0] a, b, sel,
                           output y);

    wire [1:0] temp;
    reg [1:0] inverted_sel;

    assign inverted_sel = ~sel;

    genvar i;
    generate
        for (i = 0; i < 2; i = i + 1) begin : generate_mux
            and and_gate_0(temp[i], a[i], inverted_sel);
            and and_gate_1(temp[i], b[i], sel);
        end
    endgenerate

    assign y = {temp[1], temp[0]};
endmodule

module and(input a, b,
           output y);
    assign y = a & b;
endmodule