module mux65 (input [15:0] in,
                               input [3:0] sel,
                               output out);

    reg temp;

    integer i;
    always @* begin
        temp = 1'bx;
        for (i = 0; i < 16; i = i + 1) begin
            if (sel == i)
                temp = in[i];
        end
    end

    assign out = temp;

endmodule
