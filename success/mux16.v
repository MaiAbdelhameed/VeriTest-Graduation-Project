module mux16 (input [1:0] a, sel,
                    output reg y);

    always @(*) begin
        if (sel)
            y = a[1];
        else if(!sel)
            y = a[0];
    end

endmodule