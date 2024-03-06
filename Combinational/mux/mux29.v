module mux29 (input a, b, sel,
                    output reg y);
    
    always @(*) begin
        y = (sel & b) | (~sel & a);
    end
    
endmodule