module encoder29 (input [1:0] in, output out);

    reg temp;
    always @(*) begin
        temp = (in[1]) ? 2'b10 : (in[0]) ? 2'b01 : 2'b00;
    end

    assign out = temp;
    
endmodule
