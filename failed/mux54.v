module mux54 (input [7:0] in,
                              input [2:0] sel,
                              output reg out);

    reg [7:0] temp;

    integer i;
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin
            if (sel == i)
                temp[i] = in[i];
            else
                temp[i] = 1'bx;
        end
    end 

    assign out = temp;

endmodule
