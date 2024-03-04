module mux34 (input a, b, sel,
                      reg output y);

    reg not_sel;

    always @(*) begin
        not_sel = ~sel;
        y = (a & not_sel) | (b & sel);
    end
     
endmodule