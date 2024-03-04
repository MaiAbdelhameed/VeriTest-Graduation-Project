// 4x1
module mux37 (input [3:0] a, b, c, d,
                               input [1:0] sel,
                               output y);

    wire [3:0] temp;

    assign temp = (sel == 2'b00) ? a : (sel == 2'b01) ? b : (sel == 2'b10) ? c : d;

    assign y = temp;

endmodule
