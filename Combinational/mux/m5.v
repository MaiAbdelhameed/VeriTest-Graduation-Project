module mux_behavioral(input a, b, sel,
                       reg output y);

    always @(*) begin
        if (sel)
            y = b;
        else
            y = a;
    end

endmodule