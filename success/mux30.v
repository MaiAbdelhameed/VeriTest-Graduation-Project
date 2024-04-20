module mux30 (input a, b, sel,
                    output y);
    
    reg temp_y;
    
    always @(*) begin
        temp_y = (sel & b) | (~sel & a);
    end

    assign y = temp_y;
    
endmodule