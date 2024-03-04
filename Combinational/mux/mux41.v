// 4x1
module mux41 (input [3:0] a, b, c, d,
                               input [1:0] sel,
                               output y);

    reg temp;
    
    always @(*) begin
        temp = (sel == 2'b00) ? a : (sel == 2'b01) ? b : (sel == 2'b10) ? c : d;
    end
    
    assign y = temp;

endmodule
