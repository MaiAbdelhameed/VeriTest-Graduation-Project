module ALU10(d_out1,s0,s1,c0,A,B);      
    output [3:0] d_out1;
    input s0,s1,c0;
    input [3:0] A;
    input [3:0] B;
    reg [3:0] d_out1;
    
    always @(*) 
    begin 
        if(s0 == 1'b0 & s1 == 1'b0) begin
            d_out1 = ( A & B); 
            end
        else if(s0 == 1'b1 & s1 == 1'b0) begin
            d_out1 = ( A | B); 
            end
        else if(s0 == 1'b0 & s1 == 1'b1) begin
            d_out1 = ( A ^ B); 
            end
        else begin
            d_out1 = ( A ^~ B); 
            end
    end
endmodule
