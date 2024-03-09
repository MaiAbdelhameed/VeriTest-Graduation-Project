module mux36 (input a, b, sel,
                    output y);

    reg temp_y;

    always @(*) begin
        if (sel)
            temp_y = b;
        else
            temp_y = a;
    end

    assign y = temp_y;

endmodule