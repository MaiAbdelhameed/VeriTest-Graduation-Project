module mux46(input [3:0] a, b, c, d,
                              input [1:0] sel,
                              output y);

    wire [3:0] temp;

    genvar i;
    generate
        for (i = 0; i < 4; i = i + 1) begin : generate_mux
            assign temp[i] = (sel == i) ? a[i] : (sel == i) ? b[i] : (sel == i) ? c[i] : d[i];
        end
    endgenerate

    assign y = temp;

endmodule
