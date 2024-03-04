module mux15 (input a, b, sel,
                    output reg y);

    always @(*) begin
        if (sel)
            y = b;
        else if(!sel)
            y = a;
    end

endmodule