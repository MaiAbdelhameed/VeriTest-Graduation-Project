module ALU13(d_out1,s,c0,A,B);      
    output [3:0] d_out1;
    input [1:0] s;
    input c0;
    input [3:0] A;
    input [3:0] B;
    reg [3:0] d_out1;
    
    always @(*) 
    begin
        if(s == 2'b00) begin
            d_out1 = ( A & B); 
            end
        else if(s == 2'b01) begin
            d_out1 = ( A | B); 
            end
        else if(s == 2'b10) begin
            d_out1 = ( A ^ B); 
            end
        else begin
            d_out1 = ( A ^~ B); 
            end
        end
endmodule
