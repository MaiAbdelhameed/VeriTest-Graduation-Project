module mux35 (input a, b, sel,
                    output y);

    reg not_sel;
    reg temp_y;
    always @(*) begin
        not_sel = ~sel;
        temp_y = (a & not_sel) | (b & sel);
    end
    
    assign y = temp_y;
     
endmodule