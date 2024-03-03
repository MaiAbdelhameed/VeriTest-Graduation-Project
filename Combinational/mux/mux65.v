module mux65(input [15:0] in,
                               input [3:0] sel,
                               output reg out);

    reg [15:0] temp;

    integer i;
    always @* begin
        for (i = 0; i < 16; i = i + 1) begin
            if (sel == i)
                temp[i] = in[i];
            else
                temp[i] = 1'bx;
        end
    end

    assign out = temp;

endmodule
